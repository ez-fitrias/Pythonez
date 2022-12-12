import random
import time


def computer_guess(x, y, my_number):
    low = x
    high = y
    guessing = 0
    feedback = ''
    while feedback != 'c':
        guessing += 1
        guess = random.randint(low, high)
        print(f"The computer guess {guess}")
        time.sleep(1)
        feedback = input(f"is number {guess} is too low(l), too high(h), or correct(c) ").lower()
        if feedback == 'l':
            low = guess + 1
            print("the computer is trying to guessing again")
            time.sleep(1)
        elif feedback == 'h':
            high = guess - 1
            print("the computer is trying to guessing again")
            time.sleep(1)

    print(f"the computer have guessed '{my_number}' correctly")
    time.sleep(1)
    print(f"the computer got it in {guessing} guesses ")
    time.sleep(1)
    comment = input("any words for the computer? ")
    if comment != '':
        time.sleep(1)
        print("thank you for the comment,said the computer")
        time.sleep(2)
    else:
        time.sleep(1)
        print("not a word for me?,said the computer ")
        time.sleep(2)


x, y, my_number = int(input("set a parameter(min) ")), int(input("set a parameter(max) ")), int(input("what`s your secret number? "))


computer_guess(x, y, my_number)
