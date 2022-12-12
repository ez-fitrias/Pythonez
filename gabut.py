from random import *


'''def inputs():
    global x, y
    x = int(input('set the minimum parameter '))
    y = int(input('set the maximum parameter '))
    game = input('who is the guesser, [C]omputer or [U]ser ').lower()
    if game == 'c':
        computer_guess()
    elif game == 'u':
        user_guess()


def user_guess():
    low = x
    high = y
    guesses = 0
    snum = randint(low, high)
    unum = int(input('make a guess '))
    while unum != snum:
        if unum > snum:
            print('you guessed to high, try again')
            unum = int(input('make a guess '))
            guesses += 1
        else:
            print('you guessed to low, try again')
            unum = int(input('make a guess '))
            guesses += 1
    print(f'yeay, you did it with {guesses} guesses')


def computer_guess():
    snum = int(input('what is your secret number? '))
    low = x
    high = y
    guesses = 0
    feed = ''
    guess = randint(low, high)
    while feed != 'c':
        feed = input(f'the computer guess {guess}, is {guess} too [L]ow, [H]igh or [C]orrect? ').lower()
        if feed == 'l':
            low = guess + 1
            guess = randint(low, high)
            guesses += 1
        elif feed == 'h':
            high = guess - 1
            guess = randint(low, high)
            guesses += 1
    print(f'computer made it, computer your secret number, "{snum} with {guesses} guesses"')


inputs()

width = int(input("how long(width) will it be? "))

if width % 2 != 0:                                          
    top = '|'
else:
    top = '/\\'
num = width
for i in range(int(width / 2) + 1):
    if i + 1 == 1:
        print(" " * int(num / 2) + top)
    else:
        print(" " * int((num / 2) - i ) + "/" + " " * (2 * i) + "\\" )'''

'''i = 1
while i <= 10 :
    print(i)
    i += 1'''

bil1 = int(input())
bil2 = int(input())

if bil1 == bil2:
    print('sama besar')

elif bil1 > bil2:
    print("bil1 lebih besar")

else:
    print('bil2 lebih besar')
