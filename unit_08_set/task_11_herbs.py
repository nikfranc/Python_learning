medicine_num = int(input())
med_list = set()
for i in range(medicine_num):
    herbs_num = int(input())
    for j in range(herbs_num):
        med_list.add(input())
print(*med_list, sep='\n')
