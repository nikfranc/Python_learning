town1 = input()
town2 = input()
if town1 == 'Тула' and town2 == 'Пенза' \
        or town1 == 'Тула' and town2 == 'Тула' \
        or town1 == 'Пенза' and town2 == 'Пенза': #не придумал как короче сделать
    print('НЕТ')
elif town1 == 'Тула' or town2 == 'Пенза':
    print('ДА')