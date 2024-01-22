def somar():
    print(f'Essa função vai somar valores')

def multi():
    print(f'Essa função vai multiplicar valores')

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i 
    return -1 