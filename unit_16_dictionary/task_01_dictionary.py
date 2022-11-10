dict = {}
for i in range(int(input())):
    curr_elem = str(input()).split()
    dict[curr_elem[0]] = ' '.join(curr_elem[1:])

mom_words = list()
for i in range(int(input())):
    mom_words.append(str(input()))

for i in range(len(mom_words)):
    if mom_words[i] in dict.keys():
        print(mom_words[i] + ' ' + dict[mom_words[i]])
    else:
        print('Нет в словаре')