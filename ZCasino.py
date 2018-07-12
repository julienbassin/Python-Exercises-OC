from random import randrange
from math import ceil

def main():
    amount = 1000
    continue_party = True
    bet_number = -1
    print("You will start a part with", amount, "$")
    while continue_party:
        while bet_number < 0 or bet_number > 49:
            bet_number = input("Enter a number between 0 and 49 ?")
            try:
                bet_number = int(bet_number)
            except ValueError:
                print("This is not a number")
                bet_number = -1
                continue
        bet = 0 
        while bet <= 0  or bet > amount:
            bet = input("how much do you want to bet ?")
            try:
                bet = int(bet)
            except ValueError:
                print("this is not a number")
                bet = -1
                continue
            if bet <= 0:  
                print("bet can't negative")
            if bet > amount: 
                print("bet can't be superior to your current money")
        magic_number = randrange(50)
        print("the magic number is ...", magic_number)

        if magic_number == bet_number:
            amount += bet * 3
            print("you earned three of times of your bet", bet*3, "$!")
        elif magic_number % 2 == bet_number % 2:
            print("you earned an half of your bet")
            bet = ceil(bet * 0.5)
            amount += bet
        else:
            print("you lost your bet")
            amount -= bet
        if amount <= 0:
            print("no more money , you have to leave !")
            continue_party = False
        else:
            print("it remains you ", amount, "$")
            quit = input("would you like to continue ?")
            if quit == "q" or quit == "Q":
                print("you leave the party")
                continue_party = False

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Program terminated")