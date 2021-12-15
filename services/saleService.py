from database.querys.purchaseQuery import PurchaseQuery
from database.querys.saleQuery import SaleQuery
from database.querys.stockQuery import StockQuery
from database.querys.walletQuery import WalletQuery
from stocks import get_stocks_value


class SaleService:
  def __init__(self) -> None:
    self.walletQuery = WalletQuery()
    self.stockQuery = StockQuery()
    self.purchaseQuery = PurchaseQuery()
    self.saleQuery = SaleQuery()

  def execute(self, name_wallet: str, ticker: str, qtd: int) -> list:
    qtd = int(qtd)

    response = self.walletQuery.select_wallet_by_name(name_wallet)[0]

    if len(response) > 0:
      id_wallet, _, balance, _ = response

    # First, it is checked if there is a ticker on the wallet
    stocks = self.stockQuery.select_stocks_by_wallet_id_and_ticker(id_wallet, ticker)

    if len(stocks) == 0:
      raise Exception("This wallet don't have the ticker specified.")

    id_stock = stocks[0][0]
    current_price = get_stocks_value([ticker])[ticker]['last_price'] 

    purchases_not_sold = self.purchases_not_sold_yet(id_stock)

    if qtd > len(purchases_not_sold):
      raise Exception("Was specified more quantity than the wallet has.")

    for purchase in purchases_not_sold[:qtd]:
      self.saleQuery.insert(purchase[0], current_price)

    won = qtd*current_price
    self.walletQuery.update_balance(id_wallet, balance + won) # Updating the wallet balance

    return balance, won

  def purchases_not_sold_yet(self, id_stock: int):
    purchases = self.purchaseQuery.select_purchases_by_id_stock(id_stock)
    sales = self.saleQuery.select_all()

    purchases_not_sold = list()
    purchases_already_sold_ids = [s[1] for s in sales]

    for pur in purchases:
      if pur[0] not in purchases_already_sold_ids:
        purchases_not_sold.append(pur)

    return purchases_not_sold