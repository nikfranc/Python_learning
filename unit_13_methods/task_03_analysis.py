my_str = str(input()).lower()
max_count = 0
max_symb = ''
for i in range(len(my_str)):
    if my_str[i] != max_symb and my_str[i] != ' ':
        if max_count < my_str.count(my_str[i]):
            max_count = my_str.count(my_str[i])
            max_symb = my_str[i]
        elif max_count == my_str.count((my_str[i])):
            if ord(max_symb) > ord(my_str[i]):
                max_count = my_str.count(my_str[i])
                max_symb = my_str[i]
print(max_symb)
