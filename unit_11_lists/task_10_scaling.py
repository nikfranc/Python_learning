height = int(input())
weight = int(input())
str_list = []
for i in range(height):
    curr_str = str(input())
    if i % 2 == 0:
        str_list.append(curr_str[0:len(curr_str) // 2])
print(*str_list, sep='\n')
