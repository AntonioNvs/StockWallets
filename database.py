import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'STOCK_WALLET',
  'raise_on_warnings': True
}

class Database:
  def __init__(self) -> None:
    pass

  def create_connection(self) -> None:
    self.cnx = mysql.connector.connect(**config)

    self.cursor = self.cnx.cursor()

  def close_connection(self) -> None:
    self.cnx.close()

  def execute_insert_query(self, query) -> None:
    self.create_connection()

    # Running the given query
    try:
      self.cursor.execute(query)
    except Exception as e:
      print(e.args)
      self.close_connection()
      return
    
    self.cnx.commit()

    print('The query for insert was executed with success!')
    self.close_connection()

  def execute_query_with_return(self, query) -> list:
    self.create_connection()

    myreturn = list()

    # Running the given query
    try:
      self.cursor.execute(query)
    except Exception as e:
      print(e.args)
      return []

    myresult = self.cursor.fetchall()

    # Getting the result
    for i in myresult:
      myreturn.append(i)

    return myreturn    

class WalletQuery(Database):
  def __init__(self) -> None:
    super().__init__()
    self.name_table = 'WALLET'

  def insert_wallet(self, name, balance) -> None:
    self.execute_insert_query(
      f"""
        INSERT INTO {self.name_table} (name, balance) VALUES ('{name}', {balance});
      """
    )

  def select_all(self) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table}")

  def select_from_name(self, name_wallet) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table} WHERE name = '{name_wallet}'")


class StockQuery(Database):
  def __init__(self) -> None:
    super().__init__()
    self.name_table = 'STOCKS'

  def insert_stock(self, id_wallet, ticker, quantity) -> None:
    self.execute_insert_query(
      f"""
        INSERT INTO {self.name_table} (id_wallet, ticker, quantity) VALUES ({id_wallet}, '{ticker}', {quantity});
      """
    )

  def select_all(self) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table}")

  def select_stock_by_ticker(self, ticker):
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table} WHERE ticker = {ticker}")

class TransactionsQuery(Database):
  def __init__(self) -> None:
    super().__init__()
    self.name_table = 'TRANSACTIONS'

  def insert_transactions(self, id_wallet, ticker, price, quantity, _type) -> None:
    self.execute_insert_query(
      f"""
        INSERT INTO {self.name_table} (id_wallet, ticker, price, quantity, type) VALUES ({id_wallet}, '{ticker}', {price}, {quantity}, '{_type}');
      """
    )

  def select_all(self) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table}")


  def select_transaction_by_id_wallet(self, id_wallet) -> list:
    return self.execute_query_with_return(f"SELECT * FROM {self.name_table} WHERE id_wallet = {id_wallet}")

if __name__ == '__main__':
  Database()