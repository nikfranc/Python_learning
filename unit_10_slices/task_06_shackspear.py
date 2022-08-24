myStr = str(input())
head_count = 0
max_count = 0
for i in range(1, len(myStr)):
    if myStr[i] == 'о':
        head_count += 1
    else:
        if max_count < head_count:
            max_count = head_count
        head_count = 0
print(max_count)
