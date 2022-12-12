import random
import time
import os

names = []
dis = globals()


def members():
    num = 1
    total = int(input("how many members to put? "))
    while num != total + 1:
        name = input(f"enter the {num} name ")
        names.append(name)
        num += 1
    total = int(input("how many groups? "))
    time.sleep(0.75)
    distribute(total)


def distribute(x):
    num = 1
    total = x
    os.system('cls')
    print("okay,here you go!")
    time.sleep(0.75)
    for i in range(total):
        dis[f'group {num}'] = []
        num += 1
    num = 1
    while len(names) != 0:
        name = random.choice(names)
        dis[f'group {num}'].append(name)
        names.remove(name)
        num += 1
        if num == total + 1:
            num = 1
    num = 1
    for i in range(total):
        print(f'group {num}:', ",".join(dis[f'group {num}']))
        time.sleep(0.75)
        num += 1
    retry(total, names)


def retry(x, y):
    retry = input("do you want to re-distribute?(y/n) ").lower()
    total = x
    names = y
    if retry == 'y':
        num = 1
        for i in range(total):
            names += dis[f'group {num}']
            num += 1
        time.sleep(0.75)
        distribute(total)
    else:
        time.sleep(0.75)
        print("happy grouping:)")
        time.sleep(0.75)
        out = input('press enter to exit ')
        if out == '':
            quit()


members()
