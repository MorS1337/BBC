def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def delenie(a, b):
    return a / b

def umn(a, b):
    return a * b

if __name__ == '__main__':
    a = int(input('Привет, введи первое число: '))
    b = int(input('Введи второе число: '))
    op = input('Введи знак операции (+, -, /, *): ')

    if op == '+':
        plus(a, b)
    elif op == '-':
        minus(a, b)
    elif op == '/':
        delenie(a, b)
    elif op == '*':
        umn(a, b)
    else:
        print('Неизвестная операция')