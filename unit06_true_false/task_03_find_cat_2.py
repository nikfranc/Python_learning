catFound = False
str = input()
i = 1
while str != 'СТОП':
    if ('Кот' in str or 'кот' in str) and not catFound:
        catFound = True
        foundNum = i
    str = input()
    i += 1
if catFound == True:
    print(foundNum)
else:
    print(-1)
