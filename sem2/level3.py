# поменять разделители через split и join

def use_method(s, old, new):
    return f'{new}'.join(s.split(old))

s = input('Введите свой текст: ')
old_separator = input('Введите старый разделитель: ')
new_separator = input('Введите разделитель, на который нужно поменять: ')
print(use_method(s, old_separator, new_separator))
