from database.querys.purchaseQuery import PurchaseQuery
from database.querys.stockQuery import StockQuery
from database.querys.walletQuery import WalletQuery
from services.stockService import StockService
from stocks import get_stocks_value


class PurchaseService:
  def __init__(self) -> None:
    self.walletQuery = WalletQuery()
    self.purchaseQuery = PurchaseQuery()
    self.stockQuery = StockQuery()
    
    self.stockService = StockService()

  def execute(self, name_wallet: str, ticker: str, qtd: int) -> list:
    qtd = int(qtd)

    # Reading all tickers for verification
    with open('all_tickers.txt', 'r') as src:
      tickers = src.read().split('\n')

    if ticker not in tickers:
      raise Exception('The specified ticker does not exist.')

    response = self.walletQuery.select_wallet_by_name(name_wallet)[0]

    if len(response) > 0:
      id_wallet, _, balance, _ = response

    # Get the current price of stock
    current_price = get_stocks_value([ticker])[ticker]['last_price'] 
    spent = current_price*qtd

    # Verifying if exists balance enough to buy the stocks
    if balance < spent:
      raise Exception("There isn't money enough to buy the stocks")

    all_tickers_bought = self.stockQuery.select_stocks_by_wallet_id_and_ticker(id_wallet, ticker)

    if len(all_tickers_bought) == 0:
      id_stock = self.stockService.create(id_wallet, ticker)
    else:
      id_stock = all_tickers_bought[0][0]
    
    for _ in range(qtd):
      self.purchaseQuery.insert(id_stock, current_price)

    # Updating the wallet balance
    self.walletQuery.update_balance(id_wallet, balance - spent) 

    return balance, spent