str_list = []
for i in range(int(input())):
    str_list.append((str(input())))
for i in range(len(str_list) - 1):
    for j in range(len(str_list) - 1 - i):
        if str_list[j + 1] < str_list[j]:
            str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]
print(*str_list, sep='\n')
