# Module: `accounts.py`

A self-contained Python module for managing a single user's account in a
trading-simulation platform. It supports cash deposits/withdrawals, buying and
selling shares at a price returned by `get_share_price`, and reporting on
holdings, portfolio value, profit/loss, and transaction history.

## Class: `Account`

Represents one user's account.

### Attributes

| Attribute      | Type   | Description |
|----------------|--------|-------------|
| `user_id`      | `int`  | Unique identifier for the account owner. |
| `balance`      | `float`| Current cash balance. Initialised to `0.0`. |
| `holdings`     | `dict[str, int]` | Map of stock symbol → number of shares held (e.g. `{"AAPL": 10}`). |
| `transactions` | `list[dict]` | Append-only log of every action performed on the account. |

Each entry in `transactions` is one of:

```python
{"action": "deposit",  "amount": <float>}
{"action": "withdraw", "amount": <float>}
{"action": "buy",      "symbol": <str>, "quantity": <int>, "price": <float>}
{"action": "sell",     "symbol": <str>, "quantity": <int>, "price": <float>}
```

### Methods

#### `__init__(self, user_id: int) -> None`
Creates an empty account: zero balance, no holdings, empty transaction log.

#### `deposit(self, amount: float) -> None`
Adds `amount` to `balance`.
- Raises `ValueError` if `amount <= 0`.
- Appends a `deposit` transaction.

#### `withdraw(self, amount: float) -> None`
Subtracts `amount` from `balance`.
- Raises `ValueError` if `amount <= 0`.
- Raises `ValueError` if `amount > balance` (no negative balance allowed).
- Appends a `withdraw` transaction.

#### `buy_shares(self, symbol: str, quantity: int) -> None`
Buys `quantity` shares of `symbol` at `get_share_price(symbol)`.
- Raises `ValueError` if `quantity <= 0`.
- Raises `ValueError` if `share_price * quantity > balance`.
- Reduces `balance` by the total cost and increments `holdings[symbol]`.
- Appends a `buy` transaction recording the per-share price.

#### `sell_shares(self, symbol: str, quantity: int) -> None`
Sells `quantity` shares of `symbol` at `get_share_price(symbol)`.
- Raises `ValueError` if `quantity <= 0`.
- Raises `ValueError` if `symbol` is not held or held quantity is less than `quantity`.
- Increases `balance` by the total proceeds and decrements `holdings[symbol]`.
- Removes the symbol entry entirely when the held quantity reaches `0`.
- Appends a `sell` transaction recording the per-share price.

#### `calculate_portfolio_value(self) -> float`
Returns `balance + sum(get_share_price(sym) * qty for sym, qty in holdings)`.

#### `calculate_profit_loss(self, initial_deposit: float) -> float`
Returns `calculate_portfolio_value() - initial_deposit`.

#### `get_holdings(self) -> dict`
Returns a **copy** of `holdings` (callers cannot mutate internal state).

#### `get_profit_loss(self, initial_deposit: float) -> dict`
Returns `{"profit_loss": calculate_profit_loss(initial_deposit)}`.

#### `list_transactions(self) -> list`
Returns a **copy** of the `transactions` list.

## Module function

#### `get_share_price(symbol: str) -> float`
Test stub that returns hard-coded prices and `0.0` for any unknown symbol:

| Symbol  | Price    |
|---------|----------|
| `AAPL`  | `150.0`  |
| `TSLA`  | `700.0`  |
| `GOOGL` | `2800.0` |

## Notes

- The module is self-contained: no I/O, no persistence, no external services.
- `get_share_price` is intentionally a stub so the module can be unit-tested
  deterministically (see `output/test_accounts.py`).
- A simple Gradio demo on top of this module lives in `output/app.py`.
