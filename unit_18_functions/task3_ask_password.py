def ask_password(i=1):
    my_str = str(input())
    if i != 3:
        if my_str == 'password':
            print('Пароль принят')
        else:
            ask_password(i+1)
    else:
        print('В доступе отĸазано')


ask_password()