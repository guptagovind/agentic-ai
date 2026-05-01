import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(user_id=1)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0.0)

    def test_deposit(self):
        self.account.deposit(100.0)
        self.assertEqual(self.account.balance, 100.0)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0], {'action': 'deposit', 'amount': 100.0})

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100.0)

    def test_withdraw(self):
        self.account.deposit(100.0)
        self.account.withdraw(50.0)
        self.assertEqual(self.account.balance, 50.0)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertEqual(self.account.transactions[1], {'action': 'withdraw', 'amount': 50.0})

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(50.0)

    def test_buy_shares(self):
        self.account.deposit(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(self.account.holdings['AAPL'], 2)
        self.assertEqual(len(self.account.transactions), 3)
        self.assertEqual(self.account.transactions[2], {'action': 'buy', 'symbol': 'AAPL', 'quantity': 2, 'price': 150.0})

    def test_buy_shares_insufficient_balance(self):
        self.account.deposit(100.0)
        with self.assertRaises(ValueError):
            self.account.buy_shares('AAPL', 1)

    def test_sell_shares(self):
        self.account.deposit(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.account.sell_shares('AAPL', 1)
        self.assertEqual(self.account.balance, 850.0)
        self.assertEqual(self.account.holdings['AAPL'], 1)
        self.assertEqual(len(self.account.transactions), 4)
        self.assertEqual(self.account.transactions[3], {'action': 'sell', 'symbol': 'AAPL', 'quantity': 1, 'price': 150.0})

    def test_sell_shares_insufficient_shares(self):
        self.account.deposit(1000.0)
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 1)

    def test_calculate_portfolio_value(self):
        self.account.deposit(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.calculate_portfolio_value(), 1000.0 - 300.0)

    def test_calculate_profit_loss(self):
        self.account.deposit(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.calculate_profit_loss(1000.0), -300.0)

    def test_get_holdings(self):
        self.account.deposit(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.get_holdings(), {'AAPL': 2})

    def test_list_transactions(self):
        self.account.deposit(100.0)
        self.account.withdraw(50.0)
        self.assertEqual(len(self.account.list_transactions()), 2)

if __name__ == '__main__':
    unittest.main()