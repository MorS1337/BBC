# написать upper(), lower(), capitalize()

def use_method(s: str, method: int) -> str:
    if meth == 1:
        return s.lower()
    elif meth == 2:
        return s.upper()
    elif meth == 3:
        return s.capitalize()
    else:
        return 'Неизвестный метод'
    

if __name__ == '__main__':
    s = input('Введите свой текст: ')
    meth = int(input('Введите метод ваш метод\n1 - lower()\n2 - upper()\n3 - capitalize()\n'))
    print(use_method(s, meth))
        
    