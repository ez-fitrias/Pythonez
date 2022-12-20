import random
import time
import os


def gap(sec):
    time.sleep(sec)
    os.system('cls')


# guessing game
def help():
    os.system('cls')
    ask = ''
    while ask != 'quit':
        print("guesses - show how many times you've guessing")
        print("lives - show how many chances left to guess")
        print("history - show your previous guess + status(too low/too high)")
        print("quit - back to the game")
        ask = input("> ").lower()
        if ask == 'guesses':
            done = input(f"> you've already guessed {guesses} times ")
        elif ask == 'lives':
            done = input(f'> you have {lives} chances left ')
        elif ask == 'history':
            if guesses == 0:
                done = input("> you haven't guess a number ")
            else:
                print(f'> previous numbers :')
                for i in range(len(history)):
                    print(f' {i + 1}) {history[i]}')
                done = input('')
        elif ask == 'quit':
            continue
        else:
            done = input("> invalid input")
        if done == '' or done != '':
            os.system('cls')


def guessing_game():
    os.system('cls')
    print('welcome to guessing game')
    gap(1)
    print('define the number range')
    global guesses, lives, status, history
    history = []
    minimum = input("set the lowest number : ")
    maximum = input("set the highest number : ")
    time.sleep(0.75)
    while True:
        if minimum.isnumeric() and maximum.isnumeric():
            if int(minimum) > int(maximum) or int(minimum) == int(maximum):
                enter = input("the highest number can't be lower or same as lowest number!(press enter) ")
            else:
                minimum, maximum = int(minimum), int(maximum)
                break
        else:
            enter = input('your input must be a number!(press enter) ')
        os.system('cls')
        minimum = input("set the lowest number : ")
        maximum = input("set the highest number : ")
        time.sleep(0.75)
    c_num = random.randint(minimum, maximum + 1)
    u_num = 0
    guesses = 0
    lives = 5
    status = 'unknown'
    while u_num != c_num and lives != 0:
        gap(0.75)
        print(f'you have {lives} live(s)')
        user = input("guess the computer's number or type help for information ")
        time.sleep(0.75)
        if user.isnumeric():
            u_num = int(user)
            if u_num < c_num and lives != 1:
                if c_num - u_num <= 2:
                    print("you're getting close, guess higher")
                else:
                    print("your guess was too low, guess higher")
                status = 'too low'
            elif u_num > c_num and lives != 1:
                if u_num - c_num <= 2:
                    print("you're getting close, guess lower")
                else:
                    print("your guess was too high, guess lower")
                status = 'too high'
            history.append(str(u_num) + ' - ' + " status : " + status)
            lives -= 1
            guesses += 1
        elif user.lower() == 'help':
            help()
        else:
            print("invalid input")
    gap(0.75)
    if lives != 0:
        print(f'congrats!, got it in {guesses} guesses')
    else:
        print(f'sorry, the number was {c_num}')


guessing_game()
