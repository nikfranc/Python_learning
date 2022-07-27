print('Любите ли вы котиков?')
catsLoveFlag = input()
if catsLoveFlag == 'да' or catsLoveFlag == 'нет':
    print('Умеете ли вы программировать?')
    coderFlag = input()
    if coderFlag == 'да' or coderFlag == 'нет':
        print('Вы обладаете незаурдным умом.')
    else:
        print('Ошибка')
        exit(0)
else:
    print('Ошибка')
    exit(0)
