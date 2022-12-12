from random import *

dis = globals()


def rolling():
    result = []
    dices = int(input('how many dice(s) you want '))
    nums = int(input('how many number(s) in the dice faces '))
    roll = input("press enter to roll!")
    if roll == '':
        for i in range(dices):
            dis[f'dice {i + 1} : '] = str(randint(1, nums + 1))
            result.append(dis[f'dice {i + 1} : '])
    print(','.join(result))


# rolling()

def guessing_limited():
    min = int(input('set the minimum parameter '))
    max = int(input('set the maximum parameter '))
    chances = int(input('how many chances there will be '))
    num = randint(min, max + 1)
    user_guess = ''
    guessing = 0
    while guessing < chances and user_guess != num:
        user_guess = int(input('make a guess '))
        if user_guess > num:
            print('your guess was too high, guess lower')
            guessing += 1
        elif user_guess < num:
            print('your guess was too low, guess higher')
            guessing += 1
    print(f'congratulation, you guessed the number {str(num)} within {str(guessing + 1)} guesses')

    
