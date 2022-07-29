num = int(input())
stepsNum = 0
while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
    stepsNum += 1
print(stepsNum)
