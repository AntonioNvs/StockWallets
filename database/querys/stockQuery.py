from database.database import Database

class StockQuery(Database):
  def __init__(self) -> None:
    super().__init__()
    self.name_table = 'STOCKS'

  def insert(self, id_wallet: int, ticker: str) -> int:
    return self.execute_insert_query(
      f"""
        INSERT INTO {self.name_table} (id_wallet, ticker) VALUES ({id_wallet}, '{ticker}');
      """
    )

  def select_all(self) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table}")

  def select_stock_by_ticker(self, ticker: str) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table} WHERE ticker = '{ticker}'")

  def select_stocks_by_wallet_id(self, id_wallet: int) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table} WHERE id_wallet = {id_wallet}")

  def select_stocks_by_wallet_id_and_ticker(self, id_wallet: int, ticker: str) -> list:
    return self.execute_query_with_return(
      f"SELECT * FROM {self.name_table} WHERE id_wallet = {id_wallet} AND ticker = '{ticker}'"
    )