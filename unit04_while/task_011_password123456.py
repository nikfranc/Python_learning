password = input()
if len(password) < 8:
    print('Короткий!')
    exit(0)
if '123' in password:
    print('Простой!')
    exit(0)
passCheck = input()
if password != passCheck:
    print('Различаются')
    exit(0)
print('ОК')