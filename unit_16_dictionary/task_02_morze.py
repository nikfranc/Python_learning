with open('morse.txt', 'r') as file:
    data = [x.split()[:2] for x in file.read().split('\n')]

morse_dict = {}
for strings in data:
    morse_dict[strings[0]] = strings[1]

words = str(input()).lower().split()
for word in words:
    for char in word:
        print(morse_dict[char], end='')
    print()