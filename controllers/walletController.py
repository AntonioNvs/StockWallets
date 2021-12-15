from database.walletQuery import WalletQuery


class WalletController:
  def __init__(self, walletQuery: WalletQuery) -> None:
    self.walletQuery = walletQuery

  def create_wallet(self, args: list) -> None:
    try:
      name = args[args.index('--name') + 1]
      balance = args[args.index('--balance') + 1]

    except ValueError:
      print('Some arguments (--name or --balance) do not exist on the command')
      return

    self.walletQuery.insert(name, balance)

  def show_wallet(self, args: list):
    try:
      name = args[args.index('--name') + 1]
    except ValueError:
      print('Some arguments (--name) do not exist on the command')
      return

    response = self.walletQuery.select_wallet_by_name(name)[0]

    if len(response) > 0:
      _, name, balance, _ = response
    else:
      print("There isn't wallet with this name.")

    print()
    print(f'Name: {name}')
    print(f'Balance: {balance}')

  def list_wallets(self, args: list):
    for row in self.walletQuery.select_all():
      print('\n')
      print(f'Name: {row[1]}')
      print(f'Balance: {row[2]}')

      