my_list = str(input()).split()
print([int(my_list[i]) if int(my_list[i]) > 0 else i for i in range(len(my_list))])