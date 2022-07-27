currHeight = input()
astrNum = 0
maxHeight = 0
minHeight = 3000
while currHeight != '!':
    intHeight = int(currHeight)
    if intHeight > 150 and intHeight < 190:
        astrNum += 1
    if intHeight > maxHeight:
        maxHeight = intHeight
    if intHeight < minHeight:
        minHeight = intHeight
    currHeight = input()
print(astrNum)
print(minHeight, maxHeight)