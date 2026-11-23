import random as rd 
import sys

def main():
    guess = []
    secret = rd.randint(1, 200)
    while True:
        try:
            while True:
                player = int(input("Give me your guess ::: "))
                if player < 1 or player > 200:
                    print('We need only numbers from 1 to 200 !:!:!')
                else:
                    round(player, guess)
                    break
            x = hint(player, secret)
            result(x, guess)
            if len(guess) == 10 :
                print('Game Over !!!')
                again()
        except ValueError:
            print('We need only numbers from 1 to 200 !!!!')

def round(player, guess):
    guess.append(player)

def hint(player, secret):
    if secret > player :
        return 'small'
    elif secret < player :
        return 'big'
    else:
        return 'right'

def result(x, guess):
    if x == 'small':
        print('Your guess is too small !!!')
    elif x == 'big':
        print('Your guess is too big !!!')
    else:
        print(f'Bravo, you finish after {len(guess)} guesses !!!')
        again()

def again():
    try: 
        again = input('Do you want to play again ? yes or no ::: ')
        if again == 'yes':
            main()
        elif again == 'no':
            sys.exit()
        else:
            print('we accept only yes or no min not cap !!!!')
    except ValueError:
        print('we accept only yes or no min not cap !!!!')
        
if __name__ == "__main__" :
    main()
