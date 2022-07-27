import math
bulletNum = int(input())
for i in range(bulletNum):
    numer = int(input())
    denumer = int(input())
    if i > 0:
        sumDenum = prevDenum * denumer // math.gcd(prevDenum, denumer)
        sumNum = numer * (sumDenum / denumer) + prevNum * (sumDenum / prevDenum)
        prevNum = sumNum
        prevDenum = sumDenum
    else:
        prevNum = numer
        prevDenum = denumer
print(sumNum, '/', sumDenum)