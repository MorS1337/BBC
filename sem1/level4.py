import math

class Calculator:
    def __init__(self, type: str):
        self.type = type
    
    def operation_base(self, a, b : int, op: str) -> int:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '/':
            return a / b
        elif op == '*':
            return a * b
        else:
            return 'Неизвестная операция'

    def operation_eng(self, a, b : int, op: str) -> float:
        if op == 'sqrt':
            return math.sqrt(a)
        elif op == 'cos':
            return math.cos(a)
        elif op == 'sin':
            return math.sin(a)
        else:
            return 'Неизвестная операция'
            
        

if __name__ == '__main__':
    type = int(input('Введите тип калькулятора (0 - обычный, 1 - инженерный): '))
    a = int(input('Привет, введи первое число: '))
    b = int(input('Введи второе число (можно оставить пустым): '))
    op = input('Введи знак операции (+, -, /, *): ')
    
    calc = Calculator(type)
    
    print(calc.operation_base(a, b, op))
    