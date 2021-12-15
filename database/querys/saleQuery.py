from database.database import Database

class SaleQuery(Database):
  def __init__(self) -> None:
    super().__init__()
    self.name_table = 'SALES'

  def insert(self, id_purchase: int, sale_price: float) -> int:
    return self.execute_insert_query(
      f"""
        INSERT INTO {self.name_table} (id_purchase, sale_price) VALUES ({id_purchase}, {sale_price});
      """
    )

  def select_all(self) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table}")
