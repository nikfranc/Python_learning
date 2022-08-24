max_length = int(input())
header_num = int(input())
for i in range(header_num):
    curr_header = str(input())
    if len(curr_header) > max_length:
        print(curr_header[:max_length - 3] + '...')
    else:
        print(curr_header)

