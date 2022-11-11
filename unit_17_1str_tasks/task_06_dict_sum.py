my_list = str(input()).split()
print(sum([int(list({i: my_list[i] for i in range(len(my_list))}.keys())[i])
           * int(list({i: my_list[i] for i in range(len(my_list))}.values())[i])
           for i in range(len(my_list))]))

