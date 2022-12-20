import os
import random
import string
import time

words = ['awesome', 'programming', 'indonesia', 'live', 'impossible']
word = random.choice(words)
used_letters = []
result = ''
lives = 5
while result != word and lives != 0:
    result = ''
    for letter in word:
        if letter in used_letters:
            result += letter
        else:
            result += '-'
    if result == word:
        continue
    print(f'live(s) : {lives}')
    print('letters used :', ','.join(used_letters))
    print(f'current word is {result}')
    user_letter = input('fill the letters ')
    if user_letter not in used_letters and user_letter in string.ascii_lowercase:
        used_letters.append(user_letter)
        if user_letter not in word:
            lives -= 1
    elif user_letter in used_letters:
        print('you\'ve already guessed that letter')
    else:
        print('invalid input')
    time.sleep(1)
    os.system('cls')
print('') # ucapan selamat + kata
