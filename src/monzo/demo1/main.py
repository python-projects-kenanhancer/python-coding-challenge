import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass


class EntryNotFoundError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class TransactionError(Exception):
    pass


class NoActiveTransactionError(TransactionError):
    pass


@dataclass
class TransactionBoundary:
    command_position: int
    balance: int


class TransactionCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class DepositCommand(TransactionCommand):
    def __init__(self, account: "Account", entry_id: str, amount: int):
        self.entry_id = entry_id
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account._execute_deposit(self.entry_id, self.amount)


class WithdrawCommand(TransactionCommand):
    def __init__(self, account: "Account", entry_id: str, amount: int):
        self.entry_id = entry_id
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        self.account._execute_withdraw(self.entry_id, self.amount)


class Account:
    def __init__(self, initial_balance: int = 0):
        self.committed_balance: int = initial_balance
        self.committed_entry_balances: dict[str, int] = {}

        self.transaction_balance: int = 0
        self.transaction_commands: list[TransactionCommand] = []
        self.transaction_boundaries: list[TransactionBoundary] = []

    def _get_entry_id(self) -> str:
        return f"entry-{uuid.uuid4()}"

    def _execute_deposit(self, entry_id: str, amount: int) -> None:
        self.committed_balance += amount
        self.committed_entry_balances[entry_id] = self.committed_balance

    def _execute_withdraw(self, entry_id: str, amount: int) -> None:
        self.committed_balance -= amount
        self.committed_entry_balances[entry_id] = self.committed_balance

    def _has_active_transaction(self) -> bool:
        return bool(self.transaction_boundaries)

    def _execute_all_pending_transaction_commands(self) -> None:
        for command in self.transaction_commands:
            command.execute()

    def _clear_all_transactions(self) -> None:
        self.transaction_commands = []
        self.transaction_boundaries = []
        self.transaction_balance = 0

    def _execute_and_reset_transactions(self) -> None:
        self._execute_all_pending_transaction_commands()
        self._clear_all_transactions()

    def _execute_immediately(self) -> None:
        """Execute pending commands immediately (not in a transaction)"""
        self._execute_and_reset_transactions()

    def _is_committed_entry(self, entry_id: str) -> bool:
        return entry_id in self.committed_entry_balances

    def _validate_active_transaction(self) -> None:
        if not self._has_active_transaction():
            raise NoActiveTransactionError("No active transaction")

    def _discard_current_transaction(self) -> None:
        boundary: TransactionBoundary = self.transaction_boundaries.pop()
        self.transaction_balance = boundary.balance
        self.transaction_commands = self.transaction_commands[: boundary.command_position]

    def _commit_current_transaction(self) -> None:
        # Pop the current transaction boundary
        self.transaction_boundaries.pop()
        
        # If no more boundaries (outermost transaction), execute and clear
        if not self.transaction_boundaries:
            self._execute_all_pending_transaction_commands()
            self.transaction_commands = []
            self.transaction_balance = 0

    def deposit(self, amount: int) -> str:
        if amount <= 0:
            raise InvalidAmountError(f"Amount {amount} is not positive")

        entry_id = self._get_entry_id()

        self.transaction_balance += amount
        deposit_command = DepositCommand(self, entry_id, amount)
        self.transaction_commands.append(deposit_command)

        if not self._has_active_transaction():
            self._execute_immediately()

        return entry_id

    def withdraw(self, amount: int) -> str:
        if amount <= 0:
            raise InvalidAmountError(f"Amount {amount} is not positive")

        entry_id = self._get_entry_id()

        self.transaction_balance -= amount
        withdraw_command = WithdrawCommand(self, entry_id, amount)
        self.transaction_commands.append(withdraw_command)

        if not self._has_active_transaction():
            self._execute_immediately()

        return entry_id

    def balance(self) -> int:
        return self.committed_balance + self.transaction_balance

    def balance_at(self, entry_id: str) -> int:
        if not self._is_committed_entry(entry_id):
            raise EntryNotFoundError(f"Entry ID {entry_id} not found")

        return self.committed_entry_balances[entry_id]

    def begin(self) -> None:
        current_command_position = len(self.transaction_commands)
        transaction_boundary = TransactionBoundary(
            command_position=current_command_position,
            balance=self.transaction_balance,
        )
        self.transaction_boundaries.append(transaction_boundary)

    def commit(self) -> None:
        self._validate_active_transaction()
        self._commit_current_transaction()

    def rollback(self) -> None:
        self._validate_active_transaction()
        self._discard_current_transaction()


def main():
    print("=" * 60)
    print("Test 1: Auto-commit (no transaction)")
    print("=" * 60)
    account = Account(initial_balance=0)
    entry1 = account.deposit(100)
    print(f"Deposited 100, balance: {account.balance()}")  # 100
    entry2 = account.withdraw(30)
    print(f"Withdrew 30, balance: {account.balance()}")  # 70
    print(f"Balance at {entry1}: {account.balance_at(entry1)}")  # 100
    print(f"Balance at {entry2}: {account.balance_at(entry2)}")  # 70
    
    print("\n" + "=" * 60)
    print("Test 2: Simple transaction (begin/commit)")
    print("=" * 60)
    account = Account(initial_balance=100)
    print(f"Initial balance: {account.balance()}")  # 100
    
    account.begin()
    account.deposit(50)
    account.withdraw(20)
    print(f"Balance during transaction: {account.balance()}")  # 130 (100 + 50 - 20)
    
    account.commit()
    print(f"Balance after commit: {account.balance()}")  # 130
    
    print("\n" + "=" * 60)
    print("Test 3: Transaction rollback")
    print("=" * 60)
    account = Account(initial_balance=100)
    print(f"Initial balance: {account.balance()}")  # 100
    
    account.begin()
    account.deposit(200)
    account.withdraw(50)
    print(f"Balance during transaction: {account.balance()}")  # 250
    
    account.rollback()
    print(f"Balance after rollback: {account.balance()}")  # 100 (back to original)
    
    print("\n" + "=" * 60)
    print("Test 4: Nested transactions with per-level commit")
    print("=" * 60)
    account = Account(initial_balance=100)
    print(f"Initial balance: {account.balance()}")  # 100
    
    account.begin()  # Outer transaction
    account.deposit(50)
    print(f"After deposit 50: {account.balance()}")  # 150
    
    account.begin()  # Inner transaction
    account.deposit(30)
    print(f"After nested deposit 30: {account.balance()}")  # 180
    account.commit()  # Commit inner transaction only
    
    print(f"After inner commit: {account.balance()}")  # 180 (still pending in outer)
    account.commit()  # Commit outer transaction
    print(f"After outer commit: {account.balance()}")  # 180 (now persisted)
    
    print("\n" + "=" * 60)
    print("Test 5: Nested transactions with rollback")
    print("=" * 60)
    account = Account(initial_balance=100)
    print(f"Initial balance: {account.balance()}")  # 100
    
    account.begin()  # Outer transaction
    account.deposit(50)
    print(f"After deposit 50: {account.balance()}")  # 150
    
    account.begin()  # Inner transaction
    account.deposit(30)
    print(f"After nested deposit 30: {account.balance()}")  # 180
    account.rollback()  # Rollback inner only
    
    print(f"After inner rollback: {account.balance()}")  # 150 (back to outer state)
    account.commit()  # Commit outer
    print(f"After outer commit: {account.balance()}")  # 150
    
    print("\n" + "=" * 60)
    print("Test 6: Error handling - InvalidAmountError")
    print("=" * 60)
    account = Account(initial_balance=100)
    try:
        account.deposit(0)
    except InvalidAmountError as e:
        print(f"Caught expected error: {e}")
    
    try:
        account.withdraw(-50)
    except InvalidAmountError as e:
        print(f"Caught expected error: {e}")
    
    print("\n" + "=" * 60)
    print("Test 7: Error handling - NoActiveTransactionError")
    print("=" * 60)
    account = Account(initial_balance=100)
    try:
        account.commit()  # No transaction started
    except NoActiveTransactionError as e:
        print(f"Caught expected error: {e}")
    
    try:
        account.rollback()  # No transaction started
    except NoActiveTransactionError as e:
        print(f"Caught expected error: {e}")
    
    print("\n" + "=" * 60)
    print("Test 8: Error handling - EntryNotFoundError")
    print("=" * 60)
    account = Account(initial_balance=100)
    try:
        account.balance_at("non-existent-entry-id")
    except EntryNotFoundError as e:
        print(f"Caught expected error: {e}")
    
    print("\n" + "=" * 60)
    print("Test 9: Commit inner, rollback outer")
    print("=" * 60)
    account = Account(initial_balance=100)
    print(f"Initial balance: {account.balance()}")  # 100
    
    account.begin()  # Outer
    account.deposit(50)
    print(f"After deposit 50: {account.balance()}")  # 150
    
    account.begin()  # Inner
    account.deposit(30)
    print(f"After nested deposit 30: {account.balance()}")  # 180
    account.commit()  # Commit inner level
    print(f"After inner commit: {account.balance()}")  # 180
    
    account.rollback()  # Rollback outer (discards BOTH 50 and 30!)
    print(f"After outer rollback: {account.balance()}")  # 100
    print("Note: Inner commit doesn't persist until outer commits!")
    
    print("\n" + "=" * 60)
    print("Test 10: Complex nested transactions with rollback")
    print("=" * 60)
    account = Account(initial_balance=100)
    print(f"Initial: {account.balance()}")  # 100
    
    account.begin()  # Level 1
    account.deposit(50)
    print(f"Level 1 after deposit 50: {account.balance()}")  # 150
    
    account.begin()  # Level 2
    account.deposit(20)
    print(f"Level 2 after deposit 20: {account.balance()}")  # 170
    
    account.begin()  # Level 3
    account.deposit(10)
    print(f"Level 3 after deposit 10: {account.balance()}")  # 180
    account.rollback()  # Rollback only level 3
    print(f"After level 3 rollback: {account.balance()}")  # 170
    
    account.rollback()  # Rollback level 2
    print(f"After level 2 rollback: {account.balance()}")  # 150
    
    account.commit()  # Commit all remaining (level 1)
    print(f"After final commit: {account.balance()}")  # 150
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
