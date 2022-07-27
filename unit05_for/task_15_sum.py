n = int(input())
sum = 0
for i in range(n):
    currNum = int(input())
    if i % 2 == 0:
        sum += currNum
    else:
        sum -= currNum
print(sum)