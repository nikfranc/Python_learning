strNum = int(input())
catFound = False
for i in range(strNum):
    str = input()
    if 'Кот' in str or 'кот' in str:
        catFound = True
if catFound == True:
    print('МЯУ')
else:
    print('НЕТ')

