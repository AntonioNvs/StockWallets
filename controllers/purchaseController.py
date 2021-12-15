from database.purchaseQuery import PurchaseQuery
from database.stockQuery import StockQuery
from database.walletQuery import WalletQuery
from stocks import get_stocks_value
from decimal import Decimal

class PurchaseController:
  def __init__(self, purchaseQuery: PurchaseQuery, stockQuery: StockQuery, walletQuery: WalletQuery) -> None:
    self.purchaseQuery = purchaseQuery
    self.stockQuery = stockQuery
    self.walletQuery = walletQuery

  def purchase_execution(self, args: list) -> None:
    try:
      name_wallet = args[args.index('--name_wallet') + 1]
      qtd = int(args[args.index('--quantity') + 1])
      ticker = args[args.index('--ticker') + 1]

    except ValueError:
      print('Some arguments (--name or --quantity or --ticker) do not exist on the command')
      return

    # Reading all tickers for verification
    with open('all_tickers.txt', 'r') as src:
      tickers = src.read().split('\n')

    if ticker not in tickers:
      print('The specified ticker does not exist.')
      return

    response = self.walletQuery.select_wallet_by_name(name_wallet)[0]

    if len(response) > 0:
      id_wallet, _, balance, _ = response

    current_price = get_stocks_value([ticker])[0][1] # Get the current price of stock
    spent = current_price*qtd

    # Verifying if exists balance enough to buy the stocks
    if balance < spent:
      print("There isn't money enough to buy the stocks")
      return

    all_tickers_bought = self.stockQuery.select_stock_by_ticker(ticker)
    
    if len(all_tickers_bought) == 0:
      id_stock = self.stockQuery.insert(id_wallet, ticker)
    else:
      id_stock = all_tickers_bought[0][0]
    
    for _ in range(qtd):
      self.purchaseQuery.insert(id_stock, current_price)

    self.walletQuery.update_balance(id_wallet, balance - spent) # Updating the wallet balance

    print(f'Spent: {spent}')
    print(f'New balance: {balance - spent}')

    