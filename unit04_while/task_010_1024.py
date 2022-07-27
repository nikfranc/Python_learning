num = int(input())
numDegree = 0
while num % 2 == 0:
    num /= 2
    numDegree += 1
else:
    if num != 1:
        print('НЕТ')
        exit(0)
print(numDegree)