import random as rd 
import sys

def main():
    guess = []
    secret = rd.randint(1, 200)
    while True : 
        try:
           player = int(input('Give me your guess ::: '))
           rounding(player, guess)
           hint = hints(player, secret)
           result(guess, player, secret)
           if hint == 'right' : 
               sys.exit('')
        except ValueError :
           print('!!! Put only an Number from 1 to 200 !!!')

def rounding(player, guess):
    guess.append(player)

def hints(player, secret):
    if secret >  player : 
        return 'small'
    elif secret < player :
        return 'big'
    else:
        return 'right'
def result(guess, player, secret):
    x = hints(player, secret)
    if x == 'small':
        print('Your guess is too small !!!')
    elif x == 'big':
        print('Your guess is too big !!!')
    else:
        print(f'Bravo, Your guess is correct after {len(guess)} guesses ::: {guess} ')
        
if __name__ == "__main__" :
    main()