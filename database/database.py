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

  # Return the id of the last row
  def execute_insert_query(self, query) -> int:
    self.create_connection()

    # Running the given query
    try:
      self.cursor.execute(query)
    except Exception as e:
      print(e.args)
      self.close_connection()
      return 0
    
    self.cnx.commit()

    last_id = self.cursor.lastrowid

    print('The query for insert was executed with success!')
    self.close_connection()

    return last_id

  def execute_update_query(self, query) -> None:
    self.create_connection()

    # Running the given query
    try:
      self.cursor.execute(query)
    except Exception as e:
      print(e.args)
      self.close_connection()
      return

    self.cnx.commit()

    print('The query for update was executed with success!')
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