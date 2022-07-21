print('Как настроение?')
mood = input()
if 'хорошее' in mood or 'прекрасно' in mood  or 'отлично' in mood:
    print('Отлично, у меня все тоже хорошо.')
elif 'ужасно' in mood or 'плохо'in mood or 'отвратительно' in mood:
    print('Ничего, скоро все наладится.')
else:
    print('Извини, я тебя не понимаю.')