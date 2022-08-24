message = str(input())
fav_num = int(input())
fav_letter = str(input())
if fav_num > len(message) or len(fav_letter) > 1:
    print('ОШИБКА')
elif message[fav_num - 1] == fav_letter:
    print('ДА')
else:
    print('НЕТ')