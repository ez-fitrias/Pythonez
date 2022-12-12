def numbers():
    total = int(input("how many numbers for the table? "))
    num = 1
    for i in range(total):
        if num > 1:
            print('|``' * num + '|')
            num += 1
        else:

            print("|``|" * num)
            num += 1
    print(' ``' * (num - 1))


numbers()
