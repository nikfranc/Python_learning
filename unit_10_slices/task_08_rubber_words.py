word = str(input())
length = len(word)
if length % 2 == 0:
    for i in range(len(word) // 2):
        if i == 0:
            print(' ' * (length // 2 - 1), word[length // 2 - 1:length // 2 + 1], sep='')
        else:
            print(' ' * (length // 2 - 1 - i), word[length // 2 - 1 - i], ' ' * (2 * i), word[length // 2 + i], sep='')
else:
    for i in range(len(word) // 2 + 1):
        if i == 0:
            print(' ' * (length // 2), word[length // 2], sep='')
        else:
            print(' ' * (length // 2 - i), word[length // 2 - i], ' ' * (i * 2 - 1), word[length // 2 + i], sep='')


