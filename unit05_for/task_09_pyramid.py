num = int(input())
for i in range(1, num + 1):
    for j in range(num - i + 1, 1, -1):
        print(' ', end='')
    print('*' * (i + i - 1))