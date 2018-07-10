from random import randrange
from math import ceil

Amount = 1000
Continue_party = True
bet_number = -1
bet = 0 

print("You will start a part with", Amount, "$")
while Continue_party:
    while bet_number < 0 or bet_number > 49:
        bet_number = input("Enter a number between 0 and 49 ?")
        try:
            bet_number = (int)bet_number
        except ValueError:
            print("This is not a number")
            bet_number = -1
            continue
    while bet < 0  or bet => Amount:
        bet = input(" how much do ?")
        try:
            bet = int(bet)
        except ValueError:
            print("this is not a number")
            bet = -1
            continue
    magic_number = randrange(50)

    if magic_number == bet_number:
        Amount = bet * 3
    elif magic_number % 2 == bet_number % 2:
        Amount = (ceil)bet * 0.5
    else:
        print("you lost your bet")
        Amount = Amount - bet
    
    if Amount < 0:
        print("no more money , you have to leave !")
        Continue_party = False
    else:
        