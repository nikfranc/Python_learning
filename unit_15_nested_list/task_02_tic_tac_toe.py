my_list = []
n = int(input())
for _ in range(n):
    my_list.append([char for char in str(input())])
o_win = ['o'] * 3
x_win = ['x'] * 3
for i in range(n):
    for j in range(n - 2):
        if my_list[i][j: j + 3] == o_win or [my_list[l][k] for l in range(n - 2) for k in range(n)] == o_win:
            print('o')
            exit(0)
        elif my_list[i][j: j + 3] == x_win or [my_list[l][k] for l in range(n - 2) for k in range(n)] == x_win:
            print('x')
            exit(0)
print('-')
