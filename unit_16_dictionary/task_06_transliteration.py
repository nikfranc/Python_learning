with open('literal.txt', 'r', encoding='utf-8') as file:
    data = [x.split()[1:] for x in file.read().split('\n')]
dict = {}
for i in range(len(data)):
    dict[data[i][0]] = data[i][1]
my_str = str(input()).replace('ъ', '').replace('ь', '').replace('Ъ', '').replace('Ь', '').replace('ё', 'е').replace('й', 'и')
for word in my_str.split():
    for char in word:
        if char.lower() in dict:
            if char.lower() != char:
                print(dict[char.lower()].upper(), end='')
            else:
                print(dict[char], end='')
        else:
            print(char, end='')
    print(end=' ')
