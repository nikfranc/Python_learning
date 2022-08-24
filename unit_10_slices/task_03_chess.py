length = int(input())

char_str = ''
for i in range(length):
    char_str += chr(ord('A') + i)
num_str = ''
for i in range(length):
    num_str += str(i)

for i in range(length, 0, -1):
    for j in range(length):
        print(char_str[j], num_str[i], sep='', end=' ')
    print('')




