from database.querys.walletQuery import WalletQuery
from database.querys.stockQuery import StockQuery
from database.querys.purchaseQuery import PurchaseQuery
from services.saleService import SaleService
from stocks import get_stocks_value

class ProfitAnalysis:
  def __init__(self) -> None:
    self.walletQuery = WalletQuery()
    self.stockQuery = StockQuery()
    self.purchaseQuery = PurchaseQuery()

    self.saleService = SaleService()

  def info_wallet_stocks(self, name_wallet):
    id_wallet = self.walletQuery.select_wallet_by_name(name_wallet)[0][0]

    stocks = self.stockQuery.select_stocks_by_wallet_id(id_wallet)

    tickers_stocks = set([s[2] for s in stocks])
    current_info_stocks = get_stocks_value(tickers_stocks)

    info = {}

    for s in stocks:
      ticker = s[2]
      purchases = self.saleService.purchases_not_sold_yet(s[0])

      if len(purchases) == 0: continue

      info[ticker] = {
        'spent': sum([p[2] for p in purchases]),
        'current_price': current_info_stocks[ticker]['last_price'] * len(purchases),
        'quantity': len(purchases)
      }

      info[ticker]['profit'] = ((info[ticker]['current_price'] / info[ticker]['spent']) - 1) * 100
    
    return info