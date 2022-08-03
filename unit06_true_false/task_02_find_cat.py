strNum = int(input())
catFound = False
for i in range(strNum):
    str = input()
    if 'Кот' in str or 'кот' in str:
        catFound = True
if catFound:
    print('МЯУ')
else:
    print('НЕТ')

