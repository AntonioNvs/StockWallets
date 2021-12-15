from services.purchaseService import PurchaseService
from utils.verify import verify_args

class PurchaseController:
  def __init__(self) -> None:
    self.purchaseService = PurchaseService()

  def purchase_execution(self, args: list) -> None:
    result = verify_args(args, ['--name_wallet', '--ticker', '--quantity'])
    
    # if there aren't arguments enough, is printed and the program return
    if len(result) == 0: return
    
    name_wallet, ticker, qtd = result
    
    balance, spent = self.purchaseService.execute(name_wallet, ticker, qtd)

    print(f'Spent: {spent}')
    print(f'New balance: {balance - spent}')

    