catFound = False
str = input()
i = 1
catStrNum = 0
while str != 'СТОП':
    if 'Кот' in str or 'кот' in str:
        catStrNum += 1
        if not catFound:
            catFound = True
            foundNum = i
    str = input()
    i += 1
if catFound:
    print(catStrNum, foundNum)
else:
    print(-1)