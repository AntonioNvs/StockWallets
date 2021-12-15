from database.database import Database
from decimal import Decimal

class WalletQuery(Database):
  def __init__(self) -> None:
    super().__init__()
    self.name_table = 'WALLETS'

  def insert(self, name: str, balance: float) -> int:
    return self.execute_insert_query(
      f"""
        INSERT INTO {self.name_table} (name, balance) VALUES ('{name}', {balance});
      """
    )

  def select_all(self) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table};")

  def select_wallet_by_name(self, name_wallet) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table} WHERE name = '{name_wallet}';")

  def select_wallet_by_id(self, id_wallet) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table} WHERE id = {id_wallet};")

  def update_balance(self, id_wallet: id, new_value: Decimal) -> None:
    return self.execute_update_query(
      f"""
        UPDATE {self.name_table}
        SET balance = {new_value}
        WHERE id = {id_wallet};
      """
    )