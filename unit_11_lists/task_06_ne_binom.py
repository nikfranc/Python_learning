num_list = list()
for i in range(int(input())):
    num_list.append(int(input()))
for i in range(1, len(num_list)):
    print(num_list[i] + num_list[i - 1])