from time import sleep


def insertion_sort():
    print(array)
    sleep(1)
    print('processing')
    sleep(1)
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
            print(array)
            sleep(1)
    print('done!')


array = [2, 8, 7, 16, 18, 9, 0, 1]

# insertion_sort()

def attempt():
    array = [9, 4, 5, 2, 7, 0, 1]
    for i in range(1, len(array)):
        i = j
        while array[j] < array[j - 1] and j != 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
