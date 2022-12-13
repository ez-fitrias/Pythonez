import random


def help():
    print("guesses - show how many times you've guessing")
    print("lives - show how many chances left to guess")
    print("pre - show your previous guess + status(too low/too high)")
    print("quit - back to the game")
    ask = input("> ").lower()
    while ask != 'quit':
        if ask == 'guesses':
            print(f"you've already guessed {guesses} times")
        elif ask == 'lives':
            print(f'you have {lives} chances left')
        elif ask == 'pre':
            print(f'previous number : {pre_u_num} - status : {status}')
        else:
            print("invalid input")
        ask = input("> ").lower()


min = int(input("set the minimum parameter "))
max = int(input("set the maximum parameter "))
c_num = random.randint(min, max + 1)
u_num = ''
pre_u_num = ''
guesses = 0
lives = 7
status = 'unknown'
while u_num != c_num and lives != 0:
    guesses += 1
    u_num = input("guess the computer's number or type help for information ")
    if u_num.isnumeric():
        if int(u_num) < c_num:
            print("your guess was too low, guess higher")
            pre_u_num = int(u_num)
            status = 'too low'
            lives -= 1
        elif int(u_num) > c_num:
            print("your guess was too high, guess lower")
            pre_u_num = int(u_num)
            status = 'too high'
            lives -= 1
    if u_num.lower() == 'help':
        help()
    elif u_num.isnumeric():
        print("invalid input")
print(f'congrats!, got it in {guesses} guesses')
