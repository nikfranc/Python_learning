data = [str(input()).split() for i in range(int(input()))]
dict = {}
for i in range(len(data)):
    if data[i][1] not in dict:
        dict[data[i][1]] = data[i][0]
    else:
        dict[data[i][1]] += ' ' + data[i][0]

dudes = [str(input()) for i in range(int(input()))]
for dude in dudes:
    if dude in dict:
        print(dict[dude])
    else:
        print('Нет в телефонной книге')