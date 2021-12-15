def verify_args(args: list, keys: list) -> list:
  values = []
  
  try:
    for k in keys:
      values.append(args[args.index(k) + 1])
  except ValueError:
    print(f"Some arguments ({' or '.join(keys)}) do not exist on the command")
    return []

  return values