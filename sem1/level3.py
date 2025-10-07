def operation(a, b : int, zn: str) -> int:
    if zn == '+':
        return a + b
    elif zn == '-':
        return a - b
    elif zn == '/':
        return a / b
    elif zn == '*':
        return a * b
    else:
        print('Неизвестная операция')

if __name__ == '__main__':
    a = int(input('Привет, введи первое число: '))
    b = int(input('Введи второе число: '))
    op = input('Введи знак операции (+, -, /, *): ')

    print(operation(a, b, op))