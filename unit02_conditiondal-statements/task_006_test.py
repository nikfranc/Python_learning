print('Любите ли вы котиков?')
str1 = input()
if str1 == 'да' or str1 == 'нет':
    print('Умеете ли вы программировать?')
    str2 = input()
    if str2 == 'да' or str2 == 'нет':
        print('Вы обладаете незаурдным умом.')
    else:
        print('Ошибка')
        exit(0)
else:
    print('Ошибка')
    exit(0)