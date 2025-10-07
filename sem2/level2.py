# написать upper(), lower(), capitalize()
from typing import Optional

def use_method(s: str, meth: int) -> str:
    if meth == 1:
        to_find = input('Введите строку, которую хотите найти: ')
        return f'Строка {to_find} встречается на {s.find(to_find)} индексе'
    elif meth == 2:
        old = input('Введите строку, которую хотите заменить: ')
        new = input('Введите строку, на которую хотите заменить: ')
        s = s.replace(old, new)
        return s
    elif meth == 3:
        to_count = input('Введите строку, которую хотите посчитать: ')
        return f'Строка {to_count} встречается {s.count(to_count)} раз'
    else:
        return 'Неизвестный метод'

if __name__ == '__main__':
    s = input('Введите свой текст: ')
    meth = int(input('Введите метод ваш метод\n1 - find()\n2 - replace()\n3 - count()\n'))
    print(use_method(s, meth))
    
        