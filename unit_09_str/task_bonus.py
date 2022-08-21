scale = int(input())
num = str(input())
num_10 = 0
for i in range(len(num)):
    num_10 += int(num[i]) * scale ** (len(num) - 1)
print(num_10)
