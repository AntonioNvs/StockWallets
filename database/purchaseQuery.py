from database.database import Database

class PurchaseQuery(Database):
  def __init__(self) -> None:
    super().__init__()
    self.name_table = 'PURCHASES'

  def insert(self, id_stock: int, purchase_price: float) -> int:
    return self.execute_insert_query(
      f"""
        INSERT INTO {self.name_table} (id_stock, purchase_price) VALUES ({id_stock}, {purchase_price});
      """
    )

  def select_all(self) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table}")
