# import random
import os
import time


def gap(sec):
    time.sleep(sec)
    os.system('cls')


'''# getting numbers from 0 to 100
inputNumbers = range(0, 100)
# printing 4 random numbers from the given range of numbers which are
# non-repeating using sample() function
print("4 non-repeating random numbers are:")
print(random.sample(inputNumbers, 4))'''


def biggest_number():
    numbers = [9, 4, 20, 5, 12, 1, 19, 3, 7]
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    print(f'the biggest number in the list is {greatest}')


def students():
    students = []
    grade = int(input('how many grade are they '))
    many = int(input('how many students per class '))
    for i in range(grade):
        students.append([])
    time.sleep(1)
    os.system('cls')
    for classes in range(len(students)):
        for item in range(many):
            student = input(f'type the student of grade {classes + 7} : ')
            students[classes].append(student)
        time.sleep(1)
        os.system('cls')
    level = 7
    for classes in students:
        print(f'students in grade {level} are : ' + ','.join(classes))
        time.sleep(1)
        level += 1


# unpacking :
a_list = [1, 3, 5, 7]  # can also uses tuple (1, 3, 5, 7). tuple are not changeable while list does
a, b, c, d = a_list
# same as
# a = a_list[0]
# b = a_list[1]
# c = a_list[2]
# d = a_list[3]
z = None
