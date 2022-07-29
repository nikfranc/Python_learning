answer = ''
firstBorder = 1
secondBorder = 1000
while answer != '=':
    quess = (secondBorder + firstBorder) // 2
    print(quess)
    answer = input()
    if answer == '>':
        firstBorder = quess
    else:
        secondBorder = quess


