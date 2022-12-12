from time import sleep


def selection_sort():
    print(array)
    sleep(1)
    global array2
    array2 = []
    while len(array) != 0:
        array[array.index(min(array))], array[0] = array[0], array[array.index(min(array))]
        array2.append(array[0])
        array.remove(array[0])
        print(array2, array)
        sleep(1)
    print(array2)
    

array = [8, 7, 1, 2, 5, 6, 0]
# selection_sort()

array = array2

def lowest_value():
    array = [3, 4, 0, 9, 1, 8]
    for i in range(len(array)):
        if array[i] < array[i + 1]:
            lowest = array[i]
        else:
            lowest = array[i + 1]
