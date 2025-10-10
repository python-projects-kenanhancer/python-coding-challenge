import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass


def generate_entry_id() -> str:
    """
    generate_entry_id is a helper function provided to generate a random ID
    to use for an entry. You can assume that these are completely unique
    """
    return "entry-" + str(uuid.uuid4())


@dataclass
class TransactionBoundary:
    """Represents a transaction boundary with position and cached delta snapshot"""

    command_position: int
    cached_delta_snapshot: int


class TransactionCommand(ABC):
    """Abstract base class for all transaction commands"""

    def __init__(
        self, ledger: "InMemoryLedger", entry_id: str, amount: int, balance_at_creation: int
    ):
        self.ledger = ledger  # Store reference to receiver
        self.entry_id = entry_id
        self.amount = amount
        self.balance = balance_at_creation  # The balance at the point this command was created

    @abstractmethod
    def execute(self) -> None:
        """Execute the command by invoking the appropriate ledger method"""
        pass

    @property
    @abstractmethod
    def balance_delta(self) -> int:
        """The change in balance caused by this command"""
        pass


class DepositCommand(TransactionCommand):
    """Command to encapsulate deposit method invocation"""

    def execute(self) -> None:
        self.ledger._execute_deposit(self.entry_id, self.amount)

    @property
    def balance_delta(self) -> int:
        return self.amount


class WithdrawCommand(TransactionCommand):
    """Command to encapsulate withdraw method invocation"""

    def execute(self) -> None:
        self.ledger._execute_withdraw(self.entry_id, self.amount)

    @property
    def balance_delta(self) -> int:
        return -self.amount


class InMemoryLedger:
    """
    An in-memory ledger that tracks deposits and withdrawals with transaction support.

    Public API:
        - balance() -> int
        - deposit(amount) -> str
        - withdraw(amount) -> str
        - balance_at(entry_id) -> int
        - begin() -> None
        - commit() -> None
        - rollback() -> None
    """

    # ================================================================
    # INITIALIZATION
    # ================================================================

    def __init__(self, initial_balance: int = 0):
        self.committed_balance: int = initial_balance
        self.committed_entry_ids: dict[str, int] = {}
        self.transaction_commands: list[TransactionCommand] = []
        self.transaction_boundaries: list[TransactionBoundary] = []
        self.cached_pending_delta: int = 0

    # ================================================================
    # PUBLIC API - Query Operations
    # ================================================================

    def balance(self) -> int:
        """
        Returns an int of the current total balance at this
        point in time (including pending transactions)
        """
        return self.committed_balance + self._pending_balance_delta

    def balance_at(self, entry_id: str) -> int:
        """
        Returns an int of the total balance at the point (and
        including) of a particular entry ID. If the specified entry ID
        does not exist in the ledger, it raises an EntryNotFoundError.
        """
        if self._is_committed_entry(entry_id):
            return self.committed_entry_ids[entry_id]

        return self._find_pending_entry_balance(entry_id)

    # ================================================================
    # PUBLIC API - Mutation Operations
    # ================================================================

    def deposit(self, amount: int) -> str:
        """
        Records a deposit in to the ledger for amount.
        Returns an unique entry ID string to identify the deposit.
        Raises InvalidAmountError if amount is not positive.
        """
        self._validate_amount(amount)

        entry_id = generate_entry_id()
        self.cached_pending_delta += amount
        balance_at_creation = self.committed_balance + self.cached_pending_delta
        command = DepositCommand(self, entry_id, amount, balance_at_creation)
        self.transaction_commands.append(command)

        if not self._has_active_transaction():
            self._auto_commit()

        return entry_id

    def withdraw(self, amount: int) -> str:
        """
        Records a withdrawal in to the ledger for amount.
        Returns an unique entry ID string to identify the withdrawal.
        Raises InvalidAmountError if amount is not positive.
        """
        self._validate_amount(amount)

        entry_id = generate_entry_id()
        self.cached_pending_delta -= amount
        balance_at_creation = self.committed_balance + self.cached_pending_delta
        command = WithdrawCommand(self, entry_id, amount, balance_at_creation)
        self.transaction_commands.append(command)

        if not self._has_active_transaction():
            self._auto_commit()

        return entry_id

    # ================================================================
    # PUBLIC API - Transaction Operations
    # ================================================================

    def begin(self) -> None:
        """Starts a transaction. Transactions can be nested."""
        self._mark_transaction_start()

    def commit(self) -> None:
        """
        Finishes and writes (commits) all open transactions.
        If commit is called without a transaction being started,
        it raises a TransactionError.
        """
        if not self._has_active_transaction():
            raise TransactionError

        self._execute_all_pending_commands()
        self._clear_all_transactions()

    def rollback(self) -> None:
        """
        Finishes the current active transaction but discards
        all the changes. If rollback is called without a transaction being
        started, it raises a TransactionError.
        """
        if not self._has_active_transaction():
            raise TransactionError

        self._discard_current_transaction()

    # ================================================================
    # PRIVATE - Validation
    # ================================================================

    def _validate_amount(self, amount: int) -> None:
        """Validate that the amount is positive"""
        if amount <= 0:
            raise InvalidAmountError(f"Amount must be positive, got {amount}")

    # ================================================================
    # PRIVATE - Business Logic (invoked by commands)
    # ================================================================

    def _execute_deposit(self, entry_id: str, amount: int) -> None:
        """Business logic for executing a deposit"""
        self.committed_balance += amount
        self.committed_entry_ids[entry_id] = self.committed_balance

    def _execute_withdraw(self, entry_id: str, amount: int) -> None:
        """Business logic for executing a withdrawal"""
        self.committed_balance -= amount
        self.committed_entry_ids[entry_id] = self.committed_balance

    # ================================================================
    # PRIVATE - Query Helpers
    # ================================================================

    @property
    def _pending_balance_delta(self) -> int:
        """Returns the cached total balance change from all pending commands"""
        return self.cached_pending_delta

    def _is_committed_entry(self, entry_id: str) -> bool:
        """Check if the entry exists in committed entries"""
        return entry_id in self.committed_entry_ids

    def _find_pending_entry_balance(self, entry_id: str) -> int:
        """Find and return the balance at a specific pending entry"""
        for command in self.transaction_commands:
            if command.entry_id == entry_id:
                return command.balance
        raise EntryNotFoundError

    # ================================================================
    # PRIVATE - Transaction Helpers
    # ================================================================

    @property
    def _current_command_position(self) -> int:
        """Returns the current position in the command list"""
        return len(self.transaction_commands)

    def _mark_transaction_start(self) -> None:
        """Records the start of a new transaction with a snapshot of current state"""
        boundary = TransactionBoundary(
            command_position=self._current_command_position,
            cached_delta_snapshot=self.cached_pending_delta,
        )
        self.transaction_boundaries.append(boundary)

    def _has_active_transaction(self) -> bool:
        """Check if there is at least one active transaction"""
        return bool(self.transaction_boundaries)

    def _execute_all_pending_commands(self) -> None:
        """Execute all pending commands"""
        for command in self.transaction_commands:
            command.execute()

    def _clear_all_transactions(self) -> None:
        """Clear all transaction state"""
        self.transaction_commands = []
        self.transaction_boundaries = []
        self.cached_pending_delta = 0

    def _auto_commit(self) -> None:
        """Auto-commit: execute and clear pending commands immediately"""
        self._execute_all_pending_commands()
        self._clear_all_transactions()

    def _discard_current_transaction(self) -> None:
        """Remove the current transaction and restore the cached delta snapshot"""
        boundary: TransactionBoundary = self.transaction_boundaries.pop()
        self.cached_pending_delta = boundary.cached_delta_snapshot
        self.transaction_commands = self.transaction_commands[
            : boundary.command_position
        ]


class TransactionError(BaseException):
    pass


class EntryNotFoundError(BaseException):
    pass


class InvalidAmountError(ValueError):
    pass
