str_num = int(input())
for i in range(str_num):
    curr_str = str(input())
    if 'кот' in curr_str:
        for j in range(len(curr_str) - 2):
            if curr_str[j:j + 3] == 'кот':
                cat_index = j + 1
                break
        print((i + 1), cat_index, sep=' ')