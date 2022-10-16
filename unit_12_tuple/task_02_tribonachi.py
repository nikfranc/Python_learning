num1, num2, num3 = 1, 1, 1
print(num1, num2)
for i in range(int(input())):
    print(num3, end=' ')
    num3, num2, num1 = num1 + num2 + num3, num2, num3
