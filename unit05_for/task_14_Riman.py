import math
num = int(input())
sum = 0
for i in range(1, num + 1):
    sum += 1 / (i * i)
print((math.pi * math.pi) / sum)
