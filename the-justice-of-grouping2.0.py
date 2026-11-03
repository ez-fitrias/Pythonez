import random
import os

# Process
def distributePeople(names, total_groups):
    backup_names = names.copy()  # Create a backup of the original names list, so that redistribution can be done without losing the original names
    groups = [[] for i in range(total_groups)]  # Same as:
                                                # groups = []
                                                # for i in range(total_groups):
                                                #     groups.append([])
                                                # index = 0
    
                                                # Alternative:
    while len(backup_names) > 0:                       # if index == total_groups:
        for i in range(total_groups):           #     index = 0
            if len(backup_names) == 0:                 # if len(names) == 0:
                break                           #     break
            person = random.choice(backup_names)       # person = random.choice(names)
            groups[i].append(person)            # groups[index].append(person)
            backup_names.remove(person)                # names.remove(person)
                                                # index += 1
    return groups

def catchInt(text):
    number = input(text)
    try:
        number = int(number)
        if number <= 0:
            os.system('cls')
            print("Please enter a positive integer.")
            return catchInt(text)
        else:
            return number
    except ValueError:
        if number.lower() == 'q':
            print("Exiting the program.")
            exit()
        else:
            os.system('cls')
            print("Please enter a valid integer.")
            return catchInt(text)

def yesNo(text):
    answer = input(text).lower()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("Please enter 'y' or 'n'.")
        return yesNo(text)

# Input Output
print("Welcome to the group distribution program!")
total_people = catchInt("Enter the total number of people or q to quit: ")
total_groups = catchInt("Enter the total number of groups or q to quit: ")
names = []
for i in range(total_people):
    name = input(f"Enter the name of person {i + 1}: ")
    names.append(name)

condition = True
while condition:
    print("Here are the groups:")
    groups = distributePeople(names, total_groups)
    for i, group in enumerate(groups):
        print(f"Group {i + 1}: {', '.join(group)}")
    condition = yesNo("Are you satisfied with the group distribution? Do you want to try redistributing again? (y/n): ")

print("Thank you for using the group distribution program. Happy grouping!")
