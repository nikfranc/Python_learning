n = int(input())
my_list = list()
diff_list = list()
for i in range(n):
    my_list.append(int(input()))
for i in range(n):
    for j in range(n):
        diff_list.append(my_list[i] - my_list[j])
diff_list = set(diff_list)
diff_list = list(diff_list)
diff_list.sort()
print(*diff_list)
