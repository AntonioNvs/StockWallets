from database.querys.walletQuery import WalletQuery
from services.analysis import ProfitAnalysis

class WalletService:
  def __init__(self) -> None:
    self.walletQuery = WalletQuery()

  def create(self, name: str, balance: float) -> None:
    self.walletQuery.insert(name, balance)

  def show_info_wallet(self, name) -> list:
    response = self.walletQuery.select_wallet_by_name(name)[0]

    if len(response) > 0:
      _, name, balance, _ = response
    else:
      raise Exception("There isn't wallet with this name.")

    info = ProfitAnalysis().info_wallet_stocks(name)

    return info, balance

  def list(self) -> list:
    return self.walletQuery.select_all()

