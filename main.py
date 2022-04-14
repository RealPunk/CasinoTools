import sys
import random
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
  print(Fore.BLUE + figlet_format('CasinoTools', font='slant'))
  print(Style.RESET_ALL)
  line()

loop=True

while loop==True:
    clear()
    logo()
    
    print(Fore.MAGENTA + "Welcome to CasinoTools! Please choose a casino below..." + Style.RESET_ALL)
    line()
    print(Fore.RED + "1 ~ BC.GAME" + Style.RESET_ALL)
    print(Style.RESET_ALL)
    mm1=input("> " + Fore.GREEN)
    
    if mm1=='1':
      clear()
      logo()
      print(Fore.MAGENTA + "Main Menu - BC.GAME")
      line()
      print(Fore.RED + "1 ~ Tools")
      print(Style.RESET_ALL)
      bcmm1=input("> " + Fore.GREEN)
      if bcmm1=='1':
        #tools for bc.game
        clear()
        logo()
        print(Fore.MAGENTA + "Tools - BC.GAME")
        line()
        print(Fore.RED + "1 ~ Lottery")
        print(Style.RESET_ALL)
        bclot1=input("> " + Fore.GREEN)
        if bclot1=='1':
          clear()
          logo()
          print(Fore.MAGENTA + "Lottery Tools - BC.GAME")
          line()
          print(Fore.RED + "1 ~ Lottery Odds")
          print(Fore.RED + "2 ~ Lottery Ball Generator")
          print(Fore.RED + "3 ~ Lottery Profit Calculator")
          print(Style.RESET_ALL)
          bclot2=input("> " + Fore.GREEN)
          if bclot2=='1':
            clear()
            logo()
            print(Fore.MAGENTA + "Lottery Odds - BC.GAME")
            line()
            print(Fore.GREEN + "1 BALL (Bonus Ticket)" + Style.RESET_ALL + Fore.RED + " 1 in 35")
            print(Fore.GREEN + "2 BALL (Bonus Ticket)" + Style.RESET_ALL + Fore.RED + " 1 in 595")
            print(Fore.GREEN + "3 BALL ($1)" + Style.RESET_ALL + Fore.RED + " 1 in 6,545")
            print(Fore.GREEN + "4 BALL ($20)" + Style.RESET_ALL + Fore.RED + " 1 in 52,360")
            print(Fore.GREEN + "5 BALL ($3000)" + Style.RESET_ALL + Fore.RED + " 1 in 376,992")
            line()
            input(Fore.GREEN + "Press enter to continue.")
            clear()
            print(Fore.RED + figlet_format('WARNING', font='larry3d'))
            line()
            print(Fore.RED + "The lottery is made to look like you can win (since you get a free bonus ticket). YOU WON'T WIN! You cannot get a bonus ticket on a bonus ticket. The most realistic prize is only a dollar and you have a 1 in 6,545 chance of winning. Playing dice at 1% will win you more than the lottery. Don't be taken advantage of.")
            line()
            input("Press enter to continue.")
            clear()
          if bclot2=='2':
            #lottery ball gen
            ball1 = random.randint(0,35)
            ball2 = random.randint(0,35)
            ball3 = random.randint(0,35)
            ball4 = random.randint(0,35)
            ball5 = random.randint(0,35)
            jackpotball = random.randint(0,10)

            clear()
            logo()
            print(Fore.RED + "Your generated lottery numbers are:" + Fore.GREEN)
            print(ball1, " / ", ball2, " / ", ball3, " / ", ball4, " / ",  ball5)
            line()
            print(Fore.GREEN + "Your jackpot ball is " + Fore.RED, jackpotball)
            line()
            input("Press enter to continue.")
        if bclot2=='3':
          #profit calc
          
          clear()
          logo()
          print(Fore.RED + "Please fill out the below form to calculate.")
          line()
          print(Fore.GREEN + "TIP: You can use the My Ticket tab to count up how many tickets you have bought.")
          paidtix=input(Fore.RED + "How many tickets have you bought (Not Bonus Tickets)? ")

          clear()
          logo()
          print(Fore.RED + "Please fill out the below form to calculate.")
          line()
          print(Fore.GREEN + "TIP: You can use the My Ticket tab to count up how many tickets you have bought.")
          bonustix=input(Fore.RED + "How many tickets have you bought (Bonus Tickets Only)? ")

          clear()
          logo()
          print(Fore.RED + "Please fill out the below form to calculate.")
          line()
          print(Fore.GREEN + "TIP: You can use the My Ticket tab to count up your winnings.")
          winnings=input(Fore.RED + "How much have you won combined? ")

          #analyze data

          totaltix=int(bonustix)+int(paidtix) #total amount of tickets you bought
          winningpertix=int(winnings)/totaltix #how much you have won per ticket (if every ticket won a little bit)

          #calculate if you actually won

          cost=int(paidtix)*0.1 #how much all tickets (paid only) cost you
          actualwin=int(winnings)-cost # how much you won

          if int(winnings)>cost:
            inprofit=True
          if int(winnings)<cost:
            inprofit=False

          clear()
          print(Fore.RED + figlet_format('LOTTERY', font='larry3d'))
          if inprofit==True:
            print(Fore.GREEN + "Congrats! You are in profit", actualwin, "dollars!")
          if inprofit==False:
            print(Fore.RED + "ALERT: You have lost money, your final win amount is", "%.2f" % actualwin, "dollars.")
          line()
          print(Fore.RED + "You have played" + Fore.GREEN, str(totaltix) + Fore.RED + " tickets." + Fore.GREEN, paidtix + Fore.RED + " paid tickets and" + Fore.GREEN, bonustix + Fore.RED + " bonus tickets." )
          line()
          wpt=str(winningpertix)
          print(Fore.RED + "You have won" + Fore.GREEN, "%.2f" % wpt + Fore.RED + " dollars per ticket.")
          line()
          input("Press enter to continue.")