import time
import os


def numbers():
    total = int(input("how many numbers for the table? "))
    power = int(input('how many power? for the table? '))
    num = 1
    num2 = 1
    for i in range(total):
        num3 = []
        for o in range(power):
            member = f'{num} ^ {num2} = {num ** num2}'
            num3.append(member)
            num2 += 1
        num2 = 1
        num += 1
        print("|" + '|'.join(num3) + '|')


numbers()

time.sleep(0.75)
re_make = input('want to re-make the table(y/n) ').lower()
if re_make == 'y':
    time.sleep(0.75)
    os.system('cls')
    print("okay")
    time.sleep(0.75)
    numbers()
else:
    time.sleep(0.75)
    print('happy learning')
    time.sleep(0.75)
    out = input('press enter to quit ')
    if out == '':
        quit()
