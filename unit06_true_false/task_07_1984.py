commandNum = int(input())
warCountry = 'Евразия'
peaceCountry = 'Остазия'
for i in range(commandNum):
    command = input()
    if command == 'С кем война?':
        print(warCountry)
    elif command == 'С кем мир?':
        print(peaceCountry)
    elif command == 'Меняем':
        warCountry, peaceCountry = peaceCountry, warCountry

