str_num = int(input())
for i in range(str_num):
    curr_str = str(input())
    if curr_str[:2] == '%%':
        print(curr_str[2:])
    elif curr_str[:4] == '####':
        continue
    else:
        print(curr_str)
