import uuid


def generate_entry_id() -> str:
    """
    generate_entry_id is a helper function provided to generate a random ID
    to use for an entry. You can assume that these are completely unique
    """
    return "entry-" + str(uuid.uuid4())


class InMemoryLedger:

    # Initialisation --------------------------------------------------
    def __init__(self):
        pass

    # Top Level Operations --------------------------------------------

    def balance(self) -> int:
        """
        Returns an int of the current total balance at this
        point in time
        """
        raise NotImplementedError("balance is not implemented")

    def deposit(self, amount: int) -> str:
        """
        Records a deposit in to the ledger for amount.
        Returns an unique entry ID string to identify the deposit.
        """
        raise NotImplementedError("deposit is not implemented")

    def withdraw(self, amount: int) -> str:
        """
        Records a withdrawal in to the ledger for amount.
        Returns an unique entry ID string to identify the withdrawal.
        """
        raise NotImplementedError("withdraw is not implemented")

    # Additional Operations -------------------------------------------

    def balance_at(self, entry_id: str) -> int:
        """
        Returns an int of the total balance at the point (and
        including) of a particular entry ID. If the specified entry ID
        does not exist in the ledger, it raises an EntryNotFoundError.
        """
        raise NotImplementedError("balance_at is not implemented")

    # Transaction Operations ------------------------------------------

    def begin(self):
        """
        Starts a transaction. Transactions can be nested.
        """
        raise NotImplementedError("begin is not implemented")

    def commit(self):
        """
        Finishes and writes (commits) all open transactions.
        If commit is called without a transaction being started,
        it raises a TransactionError.
        """
        raise NotImplementedError("commit is not implemented")

    def rollback(self):
        """
        Finishes the current active transaction but discards
        all the changes. If rollback is called without a transaction being
        started, it raises a TransactionError.
        """
        raise NotImplementedError("rollback is not implemented")


class TransactionError(BaseException):
    pass


class EntryNotFoundError(BaseException):
    pass
