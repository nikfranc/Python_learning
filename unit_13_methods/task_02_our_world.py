my_str = str(input()).upper().replace('','-').split(' ')
for i in range(len(my_str)):
    my_str[i] = my_str[i][1:-1]
my_str = ' '.join(my_str)
print(my_str)



