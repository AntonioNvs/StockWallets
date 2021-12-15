from commands import analyzing_command
from os import system
from time import sleep

while True:
  try:
    system('cls')

    command: str = input()

    analyzing_command(command)

    sleep(2)
    
  except KeyboardInterrupt:
    system('cls')
    print('Outing from the program in two seconds..')
    sleep(2)
    break