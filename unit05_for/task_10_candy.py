num = int(input())
minX = num
sweetsAdded = 0
for i in range(1, num // 2):
    if (num - sweetsAdded) % i == 0 and (num - sweetsAdded) // i < minX:
        minX = (num - sweetsAdded) // i
    sweetsAdded += i
print(minX)



