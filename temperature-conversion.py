

def parameter():
    global scale
    global temperature
    scale = input('which scale you want to convert,(C)elcius, (F)ahrenheit, (R)eamur, (K)elvin ').lower()    
    convertion()


def convertion():
    temperature = float(input('at which temperature? '))
    if scale == 'c':
        print(str(temperature) + 'C is equal to:')
        print(str((9/5 * temperature) + 32) + 'F')
        print(str(4/5 * temperature) + 'R')
        print(str(273.15 + temperature) + 'K')
    elif scale == 'f':
        print(str(temperature) + 'F is equal to:')
        print(str((temperature - 32) * 5 / 9) + 'C')
        print(str((temperature - 32) * 4 / 9) + 'R')
        print(str(((temperature - 32) * 5 / 9) + 273.15) + 'K')
    elif scale == 'r':
        print(str(temperature) + 'R is equal to:')
        print(str(5/4 * temperature) + 'C')
        print(str((9/4 * temperature) + 32) + 'F')
        print(str((5/4 * temperature) + 273.15) + 'K')
    elif scale == 'k':
        print(str(temperature) + 'K is equal to:')
        print(str(temperature - 273.15) + 'C')
        print(str(((temperature - 273.15) * 9/5) + 32) + 'F')
        print(str((temperature - 273.15) * 4/5) + 'R')
    else:
        print('invalid input ')
        parameter()


parameter()
