currTemp = float(input())
sum = 0
num = 0
while currTemp > -300:
    sum += currTemp
    num += 1
    currTemp = float(input())
print(sum / num)
