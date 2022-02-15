
def number_complex():
    return complex(input('number: '))

def number_float():
    return float(input('number:'))

def opern():
    return str(input('Операция +,-,*,/: '))

def out_data(data):
    if type(data) == float:
        print(f'Результат: {data:.2f}')
    else:
        print(f'Результат: {data}')