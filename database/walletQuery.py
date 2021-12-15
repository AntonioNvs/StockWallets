from database.database import Database

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

  def update_balance(self, id_wallet: id, att: float or int) -> None:
    current_balance = self.select_wallet_by_id(id_wallet)[0][2]

    return self.execute_update_query(
      f"""
        UPDATE {self.name_table}
        SET balance = {current_balance + att}
        WHERE id = {id_wallet};
      """
    )