a = int(input('Привет, введи первое число: '))
b = int(input('Введи второе число: '))
op = input('Введи знак операции (+, -, /, *): ')

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '/':
    print(a / b)
elif op == '*':
    print(a * b)
else:
    print('Неизвестная операция')