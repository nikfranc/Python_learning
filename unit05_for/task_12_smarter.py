peopleNum = int(input())
averageIQ = 0
sumIQ = 0
for i in range(1, peopleNum + 1):
    currentIQ = int(input())
    sumIQ += currentIQ
    averageIQ = sumIQ / i
    if currentIQ < averageIQ:
        print('<')
    elif currentIQ > averageIQ:
        print('>')
    else:
        print('0')