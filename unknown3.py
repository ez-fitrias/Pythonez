
import math

def odd_even_number():
    num = int(input('maximum number '))
    for i in range(num + 1):
        if i % 2 == 0:
            print(f"{i} is an even number")
        else:
            print(f"{i} is an odd number") 


def prime_number():
    par = int(input('maximum number '))
    for num in range(2,par + 1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            print(num)


def program():
    program = input("what number you want to search, [P]rime or [O]dd-even? ")
    if program == 'p'.lower():
        prime_number()
    elif program == 'o'.lower():
        odd_even_number()
    else:
        print("invalid input, try again")
        program()


program()
