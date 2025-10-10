from typing import Callable
import uuid


def generate_entry_id() -> str:
    """
    generate_entry_id is a helper function provided to generate a random ID
    to use for an entry. You can assume that these are completely unique
    """
    return "entry-" + str(uuid.uuid4())


class TransactionCommand:
    def __init__(self, type: str, function: Callable):
        self.type = type
        self.function = function

    def execute(self, ledger: "InMemoryLedger"):
        self.function(ledger)


class InMemoryLedger:
    current_balance: int
    entry_ids: dict[str, int]
    transaction_commands: list[TransactionCommand]

    # Initialisation --------------------------------------------------
    def __init__(self, initial_balance: int = 0):
        self.current_balance = initial_balance
        self.entry_ids = {}
        self.transaction_commands = []

    # Top Level Operations --------------------------------------------

    def balance(self) -> int:
        """
        Returns an int of the current total balance at this
        point in time
        """
        return self.current_balance

    def _deposit_command(self, ledger, amount: int, entry_id: str):
        """Helper method for deposit transaction command"""
        ledger.current_balance += amount
        ledger.entry_ids[entry_id] = ledger.current_balance

    def deposit(self, amount: int) -> str:
        """
        Records a deposit in to the ledger for amount.
        Returns an unique entry ID string to identify the deposit.
        """
        entry_id = generate_entry_id()
        # command = TransactionCommand(
        #     "deposit", lambda ledger: self._deposit_command(ledger, amount, entry_id)
        # )
        # self.transaction_commands.append(command)

        self.current_balance += amount
        self.entry_ids[entry_id] = self.current_balance
        return entry_id

    def withdraw(self, amount: int) -> str:
        """
        Records a withdrawal in to the ledger for amount.
        Returns an unique entry ID string to identify the withdrawal.
        """
        entry_id = generate_entry_id()
        # command = TransactionCommand(
        #     "withdraw", lambda ledger: self._withdraw_command(ledger, amount, entry_id)
        # )
        # self.transaction_commands.append(command)
        self.current_balance -= amount
        self.entry_ids[entry_id] = self.current_balance
        return entry_id

    # Additional Operations -------------------------------------------

    def balance_at(self, entry_id: str) -> int:
        """
        Returns an int of the total balance at the point (and
        including) of a particular entry ID. If the specified entry ID
        does not exist in the ledger, it raises an EntryNotFoundError.
        """

        if entry_id not in self.entry_ids:
            raise EntryNotFoundError

        total_balance = self.entry_ids[entry_id]

        return total_balance

    def _withdraw_command(self, ledger, amount: int, entry_id: str):
        """Helper method for withdraw transaction command"""
        ledger.current_balance -= amount
        ledger.entry_ids[entry_id] = ledger.current_balance



    # Transaction Operations ------------------------------------------

    def begin(self):
        """
        Starts a transaction. Transactions can be nested.
        """
        self.transaction_commands.append(TransactionCommand("begin", 0))

    def commit(self):
        """
        Finishes and writes (commits) all open transactions.
        If commit is called without a transaction being started,
        it raises a TransactionError.
        """
        for command in self.transaction_commands:
            command.execute(self)

        self.current_balance = self.entry_ids[self.transaction_commands[-1].entry_id]
        self.transaction_commands = []

    def rollback(self):
        """
        Finishes the current active transaction but discards
        all the changes. If rollback is called without a transaction being
        started, it raises a TransactionError.
        """
        self.transaction_commands = []


class TransactionError(BaseException):
    pass


class EntryNotFoundError(BaseException):
    pass
