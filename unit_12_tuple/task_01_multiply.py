num_list = []
for i in range(int(input())):
    num_list.append(int(input()))
my_num = int(input())
for i in range(len(num_list)):
    if my_num % num_list[i] == 0:
        divider = my_num // num_list[i]
        if divider in num_list[i + 1:]:
            print('ДА')
            exit(0)
print('НЕТ')
