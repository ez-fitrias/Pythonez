'''array = [5, 9, 4, 7, 2, 8, 6, 0, 1]
for i in range(1, len(array)):
    while array[i] < array[i - 1] and i != 0:
        array[i - 1], array[i] = array[i], array[i - 1]
        i -= 1
    print("".join(str(array)))'''

n = int(input("masukkan n "))
terbesar = 0
print(f"terbesar = {terbesar}")
while True:
    if n != 0:
        bilangan = int(input("masukkan bilangan "))

        if terbesar < bilangan:
            terbesar = bilangan
            n = n - 1
            print(f"n = {n}")
        else:
            n = n - 1
            print(f"n = {n}")

    else:
        print(f'terbesar = {terbesar}')
        break


