log = input()
adr = input()
if '@' in log:
    print('Некорректный логин')
if not('@' in adr):
    print('Некорректный адрес')
else:
    print('ОК')