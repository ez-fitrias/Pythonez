import math
import random


def car_game():
    user = input("> ").lower()
    status = 'unknown'
    statusflag = 'unknown'
    # main script
    while user != "quit":
        if user == statusflag:
            print(f"the car already {status}")
        elif user == "help":
            print("start - start the car")
            print("stop - stop the car")
            print("status - show current condition")
            print("quit - quit the game")
        elif user == "start":
            print("car started...ready to go")
            status = "started"
            statusflag = 'start'
        elif user == "stop":
            print("car stopped")
            status = "stopped"
            statusflag = 'stop'
        elif user == "status":
            print('current condition : ', status)
        else:
            print("I don't understand...")
        user = input("> ").lower()

# importing random module
import random
# getting numbers from 0 to 100
inputNumbers =range(0,100)
# printing 4 random numbers from the given range of numbers which are
# non-repeating using sample() function
print("4 non-repeating random numbers are:")
print(random.sample(inputNumbers, 4))
