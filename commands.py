from database import WalletQuery

wallet_query = WalletQuery()

def analyzing_command(command: str):
  first_args = {
    'create_wallet': create_wallet,
    'show_wallet': show_wallet,
    'list_wallets': list_wallets,
  }

  args = command.split()

  try:
    first_args[args[0]](args)
  except KeyError:
    print('This first command not exists')


def create_wallet(args: list):
  try:
    name_index = args.index('--name') + 1
    balance_index = args.index('--balance') + 1

  except ValueError:
    print('Some arguments (--name or --balance) do not exist on the command')
    return

  wallet_query.insert_wallet(args[name_index], args[balance_index])

def show_wallet(args: list):
  name_index = args.index('--name') + 1

  print(wallet_query.select_from_name(args[name_index]))

def list_wallets(args: list):
  for row in wallet_query.select_all():
    print('\n')
    print(f'Name: {row[1]}')
    print(f'Balance: {row[2]}')