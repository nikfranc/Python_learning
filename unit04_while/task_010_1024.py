num = int(input())
numDegree = 0
while num % 2 == 0:
    num /= 2
    numDegree += 1
if num != 1:
    print('НЕТ')
else:
    print(numDegree)