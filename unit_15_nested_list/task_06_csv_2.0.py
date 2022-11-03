my_list = []
for _ in range(int(input())):
    my_list.append([char for char in input().split(',')])
coord_list = []
n = int(input())
for i in range(n):
    coord_list.append([int(num) for num in input().split(',')])
for i in range(n):
    print(my_list[coord_list[i][0]][coord_list[i][1]])
