advert_list = list()
for i in range(int(input())):
    advert_list.append(str(input()))
num_list = list()
for i in range(int(input())):
    num_list.append(int(input()))
for num in num_list:
    print(advert_list[num - 1])
