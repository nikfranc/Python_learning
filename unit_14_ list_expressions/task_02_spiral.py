size = int(input())
myList = [[' '] * size] * size
count = 0
for i in range(size, 2):
    for j in range(size, 2):
        myList[i][j] = '*'
print(*myList, sep='\n')
