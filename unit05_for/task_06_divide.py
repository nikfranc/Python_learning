num = int(input())#
divNum = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=' ')
        divNum += 1
if divNum == 2 or num == 1:
    print('\nПРОСТОЕ')
else:
    print('\nНЕТ')