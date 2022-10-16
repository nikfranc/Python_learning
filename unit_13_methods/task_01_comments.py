str_list = list()
for i in range(int((str(input()))[1:])):
    curr_str = str(input())
    if curr_str.find('#') != -1:
        curr_str = curr_str[:curr_str.find('#') - 1]
    str_list.append(curr_str)
print(*str_list, sep='\n')
