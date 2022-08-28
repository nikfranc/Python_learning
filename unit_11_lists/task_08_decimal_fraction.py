num = int(input())
fraction_list = list()
str_convert = str((1/num))
print(str_convert)

for elem in str_convert:
    fraction_list.append(elem)

del fraction_list[0:2]
max_period = ''

for i in range(0, len(fraction_list) // 2):
    for j in range(1, len(fraction_list) // 2 + 1):
        if j + i < len(fraction_list) // 2 + 1:
            curr_slice = fraction_list[i:j + i]
            print(curr_slice, fraction_list[j + i:2 * j + i])
            if curr_slice == fraction_list[j + i:2 * j + i] and len(curr_slice) > len(max_period):
                max_period = curr_slice

if max_period == '':
    print('0')
else:
    min_period = max_period
    print('Testing for period in period:')
    for i in range(0, len(max_period) // 2):
        for j in range(1, len(max_period) // 2 + 1):
            if j + i < len(max_period) // 2 + 1:
                curr_slice = fraction_list[i:j + i]
                print(curr_slice, fraction_list[j + i:2 * j + i])
                if curr_slice == fraction_list[j + i:2 * j + i] and len(curr_slice) < len(min_period):
                    min_period = curr_slice
                    break
    print('Period = ', *min_period, sep='')
