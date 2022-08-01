str = input()
i = 1
foundNum = 0
while str != 'СТОП':
    if 'Кот' in str or 'кот' in str:
        foundNum = i
        break
    str = input()
    i += 1
if foundNum != 0:
    print(foundNum)
else:
    print(-1)
