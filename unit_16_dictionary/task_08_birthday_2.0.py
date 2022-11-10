data = [str(input()).split() for i in range(int(input()))]
dict = {}
for i in range(len(data)):
    if data[i][2] not in dict:
        dict[data[i][2]] = data[i][0] + ' ' + data[i][1]
    else:
        dict[data[i][2]] += ' ' + data[i][0] + ' ' + data[i][1]

months = [str(input()) for i in range(int(input()))]
for month in months:
    if month in dict:
        print(dict[month])
    else:
        print()