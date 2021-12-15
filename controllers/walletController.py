from services.walletService import WalletService
from utils.verify import verify_args
from time import sleep

class WalletController:
  def __init__(self) -> None:
    self.walletService = WalletService()


  def create_wallet(self, args: list) -> None:

    result = verify_args(args, ['--name', '--balance'])
    
    # if there aren't arguments enough, is printed and the program return
    if len(result) == 0: return

    name, balance = result

    try:
      name = args[args.index('--name') + 1]
      balance = args[args.index('--balance') + 1]

    except ValueError:
      print('Some arguments (--name or --balance) do not exist on the command')
      return

    self.walletService.create(name, balance)


  def show_wallet(self, args: list):
    result = verify_args(args, ['--name'])
    
    # if there aren't arguments enough, is printed and the program return
    if len(result) == 0: return
    
    name = result[0]
    
    info, balance = self.walletService.show_info_wallet(name)

    print()
    print(f'Name: {name}')
    print(f'Balance: {balance}')
    print()

    if len(info.keys()) == 0: 
      print("This wallet doesn't have stocks bought.")
      return

    for ticker in info.keys():
      print(f"Ticker: {ticker}")
      print(f"Quantity: {info[ticker]['quantity']}")
      print(f"Spent: {info[ticker]['spent']}")
      print(f"Current total: {info[ticker]['current_price']}")
      print(f"Profit: {info[ticker]['profit']}%")

      print()

    sleep(20)
    
  def list_wallets(self, args: list):
    for row in self.walletService.list():
      print('\n')
      print(f'Name: {row[1]}')
      print(f'Balance: {row[2]}')

      