class Account:
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
        self.balance = 0.0
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append({'action': 'deposit', 'amount': amount})

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount
        self.transactions.append({'action': 'withdraw', 'amount': amount})

    def buy_shares(self, symbol: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to buy shares.")
        self.balance -= total_cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        self.transactions.append({'action': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': share_price})

    def sell_shares(self, symbol: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Insufficient shares to sell.")
        share_price = get_share_price(symbol)
        total_value = share_price * quantity
        self.balance += total_value
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append({'action': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': share_price})

    def calculate_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self, initial_deposit: float) -> float:
        total_value = self.calculate_portfolio_value()
        return total_value - initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings.copy()

    def get_profit_loss(self, initial_deposit: float) -> dict:
        profit_loss = self.calculate_profit_loss(initial_deposit)
        return {'profit_loss': profit_loss}

    def list_transactions(self) -> list:
        return self.transactions.copy()

def get_share_price(symbol: str) -> float:
    prices = {
        'AAPL': 150.0,
        'TSLA': 700.0,
        'GOOGL': 2800.0
    }
    return prices.get(symbol, 0.0)