bulletNum = int(input())
for i in range(bulletNum):
    numer = int(input())
    denumer = int(input())
    if i > 0:
        if denumer > prevDenum:
            x = denumer
            y = prevDenum
        else:
            x = prevDenum
            y = denumer
        r = -1
        while r != 0:  # Евклид
            prevR = r
            r = x % y
            if r == 0:
                if prevR == -1:  # Если сразу поделилось без остатка
                    NOK = x
                else:
                    NOK = (denumer * prevDenum) // prevR
            x = y
            y = r
        sumNumer = numer * (NOK // denumer) + prevNum * (NOK // prevDenum)
        prevNum = sumNumer
        prevDenum = NOK
    else:
        prevNum = numer
        prevDenum = denumer

# Сокращение дроби
if sumNumer > NOK:
    x = sumNumer
    y = NOK
else:
    x = NOK
    y = sumNumer
r = -1
while r != 0:  # Евклид НОД
    prevR = r
    q = x // y
    r = x % y
    if r == 0:
        if prevR == -1:  # Если сразу поделилось без остатка
            NOD = y
        else:
            NOD = prevR
    x = y
    y = r


print(sumNumer // NOD, '/', NOK // NOD)




