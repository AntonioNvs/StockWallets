from database.querys.stockQuery import StockQuery

class StockService:
  def __init__(self) -> None:
    self.stockQuery = StockQuery()

  def create(self, id_wallet: int, ticker: str) -> int:
    return self.stockQuery.insert(id_wallet, ticker)