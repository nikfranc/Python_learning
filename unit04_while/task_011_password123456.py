password = input()
if len(password) < 8:
    print('Короткий!')
elif '123' in password:
    print('Простой!')
elif password != input():
    print('Различаются')
else:
    print('ОК')