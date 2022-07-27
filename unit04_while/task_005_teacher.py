coinsNum = int(input())
while coinsNum // 8 > 0:
    coinsNum //= 8
else:
    rem = coinsNum
print(rem)
