str_list = list()
for i in range(int(input())):
    str_list.append(str(input()))
char_index = int(input())
for string in str_list:
    if char_index <= len(string):
        print(string[char_index - 1], end='')
