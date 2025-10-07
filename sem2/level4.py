def use_method(s: str, meth: int) -> str:
    if meth == 1:
        to_find = input('Введите строку, которую хотите найти: ')
        return f'Строка {to_find} встречается на {s.find(to_find)} индексе'
    if meth == 2:
        old = input('Введите строку, которую хотите заменить: ')
        new = input('Введите строку, на которую хотите заменить: ')
        s = s.replace(old, new)
        return s
    if meth == 3:
        to_count = input('Введите строку, которую хотите посчитать: ')
        return f'Строка {to_count} встречается {s.count(to_count)} раз'
    if meth == 4:
        return s.lower()
    if meth == 5:
        return s.upper()
    if meth == 6:
        return s.capitalize()
    if meth == 7:
        old = input('Введите старый разделитель: ')
        new = input('Введите разделитель, на который нужно поменять: ')
        return f'{new}'.join(s.split(old))
    if meth == 8:
        b = s.isalpha()
        if b:
            return 'Строка является буквой'
        return 'Строка не является буквой'
    if meth == 9:
        b = s.isdigit()
        if b:
            return 'Строка является числом'
        return 'Строка не является числом'
    if meth == 10:
        side = input('С какой стороны убрать пробелы (R/L) или ничего не пишите: ')
        if side.lower() == 'r':
            return s.rstrip()
        if side.lower() == 'l':
            return s.lstrip()
        return s.strip()
    
    return 'Неизвестный метод'
    

if __name__ == '__main__':
    s = input('Введите свой текст: ')
    meth = int(input('Введите метод ваш метод\n1 - find()\n2 - replace()\n3 - count()\n4 - lower()\n5 - upper()\n6 - capitalize()\n7 - убрать разделитель\n8 - isalpha()\n9 - isdigit()\n10 - strip()\n'))
    print(use_method(s, meth))