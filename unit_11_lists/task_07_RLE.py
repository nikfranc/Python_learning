str_list = list(str(input()))
prev_num = str_list[0]
count = 1
for i in range(1, len(str_list)):
    curr_num = str_list[i]

    if curr_num == prev_num:
        count += 1
    else:
        print(count, prev_num)
        count = 1

    if i == len(str_list) - 1:
        print(count, curr_num)

    prev_num = curr_num
