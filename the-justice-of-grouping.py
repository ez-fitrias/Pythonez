import random
import time
import os

names = []
var = globals()


def members():
    num = 1
    groups = int(input("how many members to put? "))
    while num != groups + 1:
        name = input(f"enter the {num} name ")
        names.append(name)
        num += 1
    groups = int(input("how many groups? "))
    time.sleep(0.75)
    distribute(groups)


def distribute(x):
    num = 1
    groups = x
    os.system('cls')
    print("okay,here you go!")
    time.sleep(0.75)
    for i in range(groups):
        var[f'group {num}'] = []
        name = random.choice(names)
        var[f'group {num}'].append(name)
        names.remove(name)
        num += 1
    num = 1
    while len(names) != 0:
        name = random.choice(names)
        var[f'group {num}'].append(name)
        names.remove(name)
        num += 1
        if num == groups + 1:
            num = 1
    num = 1
    for i in range(groups):
        print(f'group {num}:', ",".join(var[f'group {num}']))
        time.sleep(0.75)
        num += 1
    retry(groups, names)


def retry(x, y):
    retry = input("do you want to re-distribute?(y/n) ").lower()
    total = x
    names = y
    if retry == 'y':
        num = 1
        for i in range(total):
            names += var[f'group {num}']
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
