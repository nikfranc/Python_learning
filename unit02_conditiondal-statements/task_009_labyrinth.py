print('Вы находитесь в пещере на развилке. Вы можете пойти "налево", "направо" или "прямо".')
print('Введите одно из слов в кавычках для выбора.')
asw1 = input()
if asw1 == 'налево':
    print('Тупик.')
    exit(0)
elif asw1 == 'направо':
    print('Поздравляю! Вы нашли выход.')
    exit(0)
elif asw1 == 'прямо':
    print('Вы вышли к еще одной развилке. Вы можете пойти "налево" или "направо".')
    asw2 = input()
    if asw2 == 'налево':
        print('Вы смело открыли правую дверь. Но за ней вас подстерегала гигантская подземная жаба, '
              'которая проглотила вас целиком!')
        print('''Вы смело открыли правую дверь.
        Но за ней вас подстерегала гигантская подземная жаба,
        которая проглотила вас целиком!''')
        exit(0)
    elif asw2 == 'направо':
        print('Вы нашли сундук с сокровищами.')
        exit(0)
    else:
        print('Ошибка')
        exit(0)
else:
    print('Ошибка')
    exit(0)
