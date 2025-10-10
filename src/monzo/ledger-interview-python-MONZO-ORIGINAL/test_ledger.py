import unittest
from ledger import InMemoryLedger, EntryNotFoundError, TransactionError


class TestInMemoryLedger(unittest.TestCase):
    def test_simple_deposit(self):
        """
        Goes through depositing some money and expecting
        it to be present and correct
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        d1 = ledger.deposit(100)
        self.assertTrue(len(d1) > 0, "entry_id was empty")
        self.assertEqual(ledger.balance(), 100)

    def test_simple_withdrawal(self):
        """
        Goes through withdrawing some money and expecting
        the balance to be reflected appropriately
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        w1 = ledger.withdraw(100)
        self.assertTrue(len(w1) > 0, "entry_id was empty")
        self.assertEqual(ledger.balance(), -100)

    def test_simple_balance_1(self):
        """
        Goes through a chain of making a deposit and withdrawal
        to assert that the flow works correctly
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        d1 = ledger.deposit(100)
        self.assertTrue(len(d1) > 0, "entry_id was empty")
        self.assertEqual(ledger.balance(), 100)

        w1 = ledger.withdraw(10)
        self.assertNotEqual(w1, d1, "entry_ids were equal")
        self.assertEqual(ledger.balance(), 90)

    def test_simple_balance_2(self):
        """
        Goes through a chain of making a withdrawal and deposit
        to assert that the flow works correctly
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        w1 = ledger.withdraw(10)
        self.assertTrue(len(w1) > 0, "entry_id was empty")
        self.assertEqual(ledger.balance(), -10)

        d1 = ledger.deposit(100)
        self.assertNotEqual(w1, d1, "entry_ids were equal")
        self.assertEqual(ledger.balance(), 90)

    def test_balance_at(self):
        """
        Asserts that we are correctly tracking balances between
        operations correctly, so we can retrieve balances at a point in time
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        d1 = ledger.deposit(100)
        self.assertEqual(ledger.balance(), 100)

        balance = ledger.balance_at(d1)
        self.assertEqual(balance, 100)

        w1 = ledger.withdraw(10)
        self.assertNotEqual(d1, w1, "entry_ids were equal")
        self.assertEqual(ledger.balance(), 90)

        balance = ledger.balance_at(d1)
        self.assertEqual(balance, 100)

        balance2 = ledger.balance_at(w1)
        self.assertEqual(balance2, 90)

    def test_balance_at_invalid_id(self):
        """
        Ensures that a bad entry ID results in an error
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)
        with self.assertRaises(EntryNotFoundError):
            ledger.balance_at("BAD_ID")

    def test_transaction_flow(self):
        """
        Goes through a simple transaction flow
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        # Start our transaction
        ledger.begin()

        # Make a deposit and a withdrawal
        d1 = ledger.deposit(100)
        w1 = ledger.withdraw(10)

        self.assertNotEqual(d1, w1, "entry_ids were equal")
        self.assertEqual(ledger.balance(), 90)

        # Commit our transaction
        ledger.commit()

        # Expect all of it to have been written appropriately
        self.assertEqual(ledger.balance(), 90)

        balance = ledger.balance_at(d1)
        self.assertEqual(balance, 100)

        balance2 = ledger.balance_at(w1)
        self.assertEqual(balance2, 90)

    def test_transaction_rollback(self):
        """
        Tests writing a transaction and then calling
        rollback, making sure that nothing is committed
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        # Start our transaction
        ledger.begin()

        # Make a deposit and a withdrawal
        d1 = ledger.deposit(100)
        w1 = ledger.withdraw(10)

        self.assertEqual(ledger.balance(), 90)
        self.assertNotEqual(w1, d1, "entry_ids were equal")

        # Rollback our transaction
        ledger.rollback()

        # Expect none of it to have been written
        self.assertEqual(ledger.balance(), 0)

        with self.assertRaises(EntryNotFoundError):
            ledger.balance_at(d1)

        with self.assertRaises(EntryNotFoundError):
            ledger.balance_at(w1)

    def test_transaction_nested(self):
        """
        Tests writing nested transactions with commit
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        # Start our transaction, create a deposit
        ledger.begin()
        d1 = ledger.deposit(100)

        # Create a new transaction
        ledger.begin()
        w1 = ledger.withdraw(10)
        self.assertEqual(ledger.balance(), 90)

        # Commit
        ledger.commit()

        # Expect all our data to be written
        self.assertEqual(ledger.balance(), 90)

        balance = ledger.balance_at(d1)
        self.assertEqual(balance, 100)

        balance2 = ledger.balance_at(w1)
        self.assertEqual(balance2, 90)

    def test_transaction_nested_rollback(self):
        """
        Tests writing nested transactions with a
        rollback before committing
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        # Start our transaction, create a deposit
        ledger.begin()
        d1 = ledger.deposit(100)

        # Create a new transaction but roll it back
        ledger.begin()
        w1 = ledger.withdraw(10)
        self.assertEqual(ledger.balance(), 90)
        ledger.rollback()

        # Expect only d1 to be written
        self.assertEqual(ledger.balance(), 100)
        balance = ledger.balance_at(d1)
        self.assertEqual(balance, 100)

        with self.assertRaises(EntryNotFoundError):
            ledger.balance_at(w1)

        # Do a commit, expect only d1 again
        ledger.commit()
        self.assertEqual(ledger.balance(), 100)
        balance = ledger.balance_at(d1)
        self.assertEqual(balance, 100)

        with self.assertRaises(EntryNotFoundError):
            ledger.balance_at(w1)

    def test_transaction_nested_full_rollback(self):
        """
        Tests writing nested transactions but
        with all transactions rolled back, we expect nothing to be written
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        # Start our transaction, create a deposit
        ledger.begin()
        d1 = ledger.deposit(100)

        # Create a new transaction
        ledger.begin()
        w1 = ledger.withdraw(10)

        # Now roll back both our transactions
        ledger.rollback()
        ledger.rollback()

        # We shouldn't be in a transaction, so expect an error
        self.assertEqual(ledger.balance(), 0)

        with self.assertRaises(TransactionError):
            ledger.commit()

        # Make sure we didn't write w1 or d1
        self.assertEqual(ledger.balance(), 0)

        with self.assertRaises(EntryNotFoundError):
            ledger.balance_at(d1)

        with self.assertRaises(EntryNotFoundError):
            ledger.balance_at(w1)

    def test_transaction_inactive_error(self):
        """
        Tests for appropriate errors if commit
        or rollback are called outside of a transaction
        """
        ledger = InMemoryLedger()
        self.assertEqual(ledger.balance(), 0)

        # Commit outside an active transaction should cause an error
        with self.assertRaises(TransactionError):
            ledger.commit()

        # Rollback outside an active transaction should cause an error
        with self.assertRaises(TransactionError):
            ledger.rollback()


if __name__ == '__main__':
    unittest.main()
