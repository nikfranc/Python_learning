lib_num = int(input())
list_num = int(input())
lib_set = set()
list_set = set()

for i in range(lib_num):
    lib_set.add(input())

for i in range(list_num):
    list_set.add(input())

for elem in list_set:
    if elem in lib_set:
        print('YES')
    else:
        print('NO')