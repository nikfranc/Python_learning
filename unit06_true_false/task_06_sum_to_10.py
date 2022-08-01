sum = 0
currNum = int(input())
sum_is_ten = False
i = 1
while currNum != 0:
    sum += currNum
    currNum = int(input())
    if sum == 10 and not sum_is_ten:
        sum_is_ten = True
        termNum = i
    i += 1
print(termNum)
