k = int(input())
l = int(input())
my_list = [[0] * k for l in range(10)]
x = int(input())
y = int(input())
power = int(input())
curr_pow = power
my_list[y][x] = power
for i in range(k):
    for j in range(l):
        curr_pow = curr_pow**((1/2)**(x-j))
        if curr_pow == int(curr_pow) and x > j:
            my_list[i][j] = curr_pow

