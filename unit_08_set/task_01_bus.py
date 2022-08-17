curr_num = input()
num_set_1 = set()
while curr_num != '':
    num_set_1.add(int(curr_num))
    curr_num = input()

curr_num = input()
num_set_2 = set()
while curr_num != '':
    num_set_2.add(int(curr_num))
    curr_num = input()

if len(num_set_1 & num_set_2) > 0:
    print(*(num_set_1 & num_set_2), sep='\n')
else:
    print('EMPTY')
