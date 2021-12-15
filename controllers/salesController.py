from services.saleService import SaleService
from utils.verify import verify_args

class SalesController:
  def __init__(self) -> None:
    self.saleService = SaleService()

  def sale_execution(self, args: list) -> None:
    result = verify_args(args, ['--name_wallet', '--ticker', '--quantity'])
    
    # if there aren't arguments enough, is printed and the program return
    if len(result) == 0: return
    
    name_wallet, ticker, qtd = result
    
    balance, won = self.saleService.execute(name_wallet, ticker, qtd)

    print(f'Won: {won}')
    print(f'New balance: {balance + won}')