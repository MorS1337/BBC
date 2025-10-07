s = '   pYthon;is;AWesome;   '

for ch in s:
    if not ch.isalpha():
        s = s.replace(ch, ' ')

s = s.strip()
print(s.lower().capitalize())