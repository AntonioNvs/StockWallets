from database.purchaseQuery import PurchaseQuery
from database.saleQuery import SaleQuery
from database.stockQuery import StockQuery
from database.walletQuery import WalletQuery
from stocks import get_stocks_value


class SalesController:
  def __init__(self, walletQuery: WalletQuery, stockQuery: StockQuery, purchaseQuery: PurchaseQuery, saleQuery: SaleQuery) -> None:
    self.walletQuery = walletQuery
    self.stockQuery = stockQuery
    self.purchaseQuery = purchaseQuery
    self.saleQuery = saleQuery

  def sale_execution(self, args: list) -> None:
    try:
      name_wallet = args[args.index('--name_wallet') + 1]
      qtd = int(args[args.index('--quantity') + 1])
      ticker = args[args.index('--ticker') + 1]

    except ValueError:
      print('Some arguments (--name or --quantity or --ticker) do not exist on the command')
      return
    
    response = self.walletQuery.select_wallet_by_name(name_wallet)[0]

    if len(response) > 0:
      id_wallet, _, balance, _ = response

    # First, it is checked if there is a ticker on the wallet
    stocks = self.stockQuery.select_stocks_by_wallet_id_and_ticker(id_wallet, ticker)

    if len(stocks) == 0:
      print("This wallet don't have the ticker specified.")

    id_stock = stocks[0][0]

    purchases = self.purchaseQuery.select_purchases_by_id_stock(id_stock)
    sales = self.saleQuery.select_all()

    # Get the current price of stock
    current_price = get_stocks_value([ticker])[0][1] 

    purchases_not_sold = list()
    purchases_already_sold_ids = [s[1] for s in sales]

    for pur in purchases:
      if pur[0] not in purchases_already_sold_ids:
        purchases_not_sold.append(pur)

    for purchase in purchases_not_sold[:qtd]:
      self.saleQuery.insert(purchase[0], current_price)

    won = qtd*current_price
    self.walletQuery.update_balance(id_wallet, balance + won) # Updating the wallet balance

    print(f'Won: {won}')
    print(f'New balance: {balance + won}')