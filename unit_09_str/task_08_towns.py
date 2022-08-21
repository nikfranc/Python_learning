first_town = str(input())
second_town = str(input())
if first_town[-1] == 'ь':
    if first_town[-2] == second_town[0]:
        print('ВЕРНО')
    else:
        print('НЕВЕРНО')
elif first_town[-1] == second_town[0]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')



