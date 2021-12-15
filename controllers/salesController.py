from database.purchaseQuery import PurchaseQuery
from database.saleQuery import SaleQuery
from database.stockQuery import StockQuery


class SalesController:
  def __init__(self, stockQuery: StockQuery, purchaseQuery: PurchaseQuery, saleQuery: SaleQuery) -> None:
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