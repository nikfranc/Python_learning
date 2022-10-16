stud_list = []
for i in range(int(input())):
    curr_stud = str(input())
    stud_list.append((curr_stud[:-2], curr_stud[-1]))
for i in range(len(stud_list)):
    print(stud_list[i][0], stud_list[i][1], sep='\t')
print('')
for i in range(len(stud_list)):
    if int(stud_list[i][1]) > 3:
        print(stud_list[i][0], stud_list[i][1], sep='\t')

