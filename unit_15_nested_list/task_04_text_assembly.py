my_list = [[int(i) for i in input().split()], [str(char) for char in input().split()]]
first = True
for i in my_list[0]:
    if first:
        print(my_list[1][i - 1].capitalize(), end=' ') # не работает capitalize
        first = False
    else:
        print(my_list[1][i - 1].lower(), end=' ')
