from database.stockQuery import StockQuery
from database.walletQuery import WalletQuery


class StockController:
  def __init__(self, walletQuery: WalletQuery, stockQuery: StockQuery) -> None:
    self.walletQuery = walletQuery
    self.stockQuery = stockQuery
    