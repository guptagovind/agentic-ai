import gradio as gr
from accounts import Account, get_share_price

account = Account(user_id=1)
initial_deposit = 0.0

def create_account(deposit):
    global initial_deposit
    account.deposit(deposit)
    initial_deposit = deposit
    return f"Account created with deposit: ${deposit}"

def deposit_funds(amount):
    account.deposit(amount)
    return f"Deposited: ${amount}. Current balance: ${account.balance}"

def withdraw_funds(amount):
    try:
        account.withdraw(amount)
        return f"Withdrew: ${amount}. Current balance: ${account.balance}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_shares(symbol, int(quantity))
        return f"Bought {quantity} shares of {symbol}. Current balance: ${account.balance}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_shares(symbol, int(quantity))
        return f"Sold {quantity} shares of {symbol}. Current balance: ${account.balance}"
    except ValueError as e:
        return str(e)

def portfolio_value():
    value = account.calculate_portfolio_value()
    return f"Total portfolio value: ${value}"

def profit_loss():
    profit_loss = account.calculate_profit_loss(initial_deposit)
    return f"Profit/Loss: ${profit_loss}"

def holdings():
    holdings = account.get_holdings()
    return holdings

def transactions():
    trans = account.list_transactions()
    return trans

with gr.Blocks() as demo:
    gr.Markdown("## Trading Simulation Account Management")
    
    with gr.Tab("Account Creation"):
        deposit_amount = gr.Number(label="Initial Deposit Amount", value=1000.0)
        create_button = gr.Button("Create Account")
        create_output = gr.Textbox(label="Result", interactive=False)
        create_button.click(create_account, inputs=deposit_amount, outputs=create_output)

    with gr.Tab("Deposit Funds"):
        deposit_funds_amount = gr.Number(label="Deposit Amount")
        deposit_button = gr.Button("Deposit")
        deposit_output = gr.Textbox(label="Result", interactive=False)
        deposit_button.click(deposit_funds, inputs=deposit_funds_amount, outputs=deposit_output)

    with gr.Tab("Withdraw Funds"):
        withdraw_funds_amount = gr.Number(label="Withdraw Amount")
        withdraw_button = gr.Button("Withdraw")
        withdraw_output = gr.Textbox(label="Result", interactive=False)
        withdraw_button.click(withdraw_funds, inputs=withdraw_funds_amount, outputs=withdraw_output)
    
    with gr.Tab("Buy Shares"):
        buy_symbol = gr.Textbox(label="Stock Symbol (AAPL, TSLA, GOOGL)")
        buy_quantity = gr.Number(label="Quantity to Buy")
        buy_button = gr.Button("Buy Shares")
        buy_output = gr.Textbox(label="Result", interactive=False)
        buy_button.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_output)

    with gr.Tab("Sell Shares"):
        sell_symbol = gr.Textbox(label="Stock Symbol (AAPL, TSLA, GOOGL)")
        sell_quantity = gr.Number(label="Quantity to Sell")
        sell_button = gr.Button("Sell Shares")
        sell_output = gr.Textbox(label="Result", interactive=False)
        sell_button.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_output)

    with gr.Tab("Portfolio Value"):
        value_button = gr.Button("Get Portfolio Value")
        value_output = gr.Textbox(label="Result", interactive=False)
        value_button.click(portfolio_value, outputs=value_output)
    
    with gr.Tab("Profit/Loss"):
        profit_loss_button = gr.Button("Calculate Profit/Loss")
        profit_loss_output = gr.Textbox(label="Result", interactive=False)
        profit_loss_button.click(profit_loss, outputs=profit_loss_output)

    with gr.Tab("Holdings"):
        holdings_button = gr.Button("Get Holdings")
        holdings_output = gr.JSON(label="Holdings")
        holdings_button.click(holdings, outputs=holdings_output)

    with gr.Tab("Transactions"):
        transactions_button = gr.Button("View Transactions")
        transactions_output = gr.JSON(label="Transactions")
        transactions_button.click(transactions, outputs=transactions_output)

demo.launch()