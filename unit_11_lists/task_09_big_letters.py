a_list = [' ', '*', ' ', '*', ' ', '*', '*', '*', '*', '*', ' ', '*', '*', ' ', '*']
b_list = ['*', '*', '*', '*', ' ', '*', '*', '*', '*', '*', ' ', '*', '*', '*', '*']
c_list = ['*', '*', '*', '*', ' ', '*', '*', ' ', ' ', '*', ' ', '*', '*', '*', '*']
my_str = str(input())
for i in range(5):
    for j in range(len(my_str)):
        if my_str[j] == 'A':
            print(*a_list[i * 3: i * 3 + 3], end='  ')
        elif my_str[j] == 'B':
            print(*b_list[i * 3: i * 3 + 3], end='  ')
        elif my_str[j] == 'C':
            print(*c_list[i * 3: i * 3 + 3], end='  ')
    print('\n')