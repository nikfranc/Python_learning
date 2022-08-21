word = str(input())
for char in word:
    if char == word[-1]:
        print(ord(char), end='')
    else:
        print(ord(char), end=', ')