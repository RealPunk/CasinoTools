import sys
from colorama import init
from colorama import Fore, Back, Style
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format
from os import system, name

def line():
  print("") #i hate typing this out for line breaks, so i do this

#credits to https://www.geeksforgeeks.org/clear-screen-python/ for saving me time writing this haha

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def logo():
  print(Fore.BLUE + figlet_format('CasinoFuck', font='slant'))
  print(Style.RESET_ALL)
  line()

clear()
logo()

print(Fore.MAGENTA + "Welcome to CasinoFuck! Please choose a casino below..." + Style.RESET_ALL)
line()
print(Fore.RED + "1 ~ BC.GAME" + Style.RESET_ALL)
line()
mm1=input("> ")

if mm1=='1':
  clear()
  logo()
  print(Fore.MAGENTA + "Main Menu - BC.GAME")
  line()
  print(Fore.RED + "1 ~ Tools")
  line()
  bcmm=input("> ")

  if bcmm1=='1':
    #tools for bc.game
    clear()
    logo()
    print(Fore.MAGENTA + "Tools - BC.GAME")
    line()
    print(Fore.RED + "1 ~ Lottery")
    line()
    bclot1=input("> ")
    if bclot1=='1':
      #chances in menu
      