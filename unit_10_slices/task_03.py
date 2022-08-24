boardSize = int(input())
boardLetter = 'ABCDEFGHI'[:boardSize]
boardNumber = '123456789'[boardSize - 1::-1]
for numbers in boardNumber:
    for letters in boardLetter:
        print(letters + numbers, end=' ')
    print('')
