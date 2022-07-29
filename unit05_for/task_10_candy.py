num = int(input())
sum = 0
peopleNum = 1
x = 2
while x > 1:
    if (num - sum) % peopleNum == 0:
        x = (num - sum) // peopleNum
    sum += 1
    peopleNum += sum
print(x)