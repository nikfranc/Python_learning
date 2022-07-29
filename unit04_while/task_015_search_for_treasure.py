treasureX = int(input())
treasureY = int(input())
direction = 'север'
myCommand = input()
iters = 0
found = 1
x = 0
y = 0
while myCommand != 'стоп':
    if myCommand == 'направо':
        if direction == 'север':
            direction = 'восток'
        elif direction == 'восток':
            direction = 'юг'
        elif direction == 'юг':
            direction = 'запад'
        else:
            direction = 'север'

    elif myCommand == 'налево':
        if direction == 'север':
            direction = 'запад'
        elif direction == 'запад':
            direction = 'юг'
        elif direction == 'юг':
            direction = 'восток'
        else:
            direction = 'север'

    elif myCommand == 'разворот':
        if direction == 'север':
            direction = 'юг'
        elif direction == 'запад':
            direction = 'восток'
        elif direction == 'юг':
            direction = 'север'
        else:
            direction = 'запад'

    elif myCommand == 'вперед':
        steps = int(input())
        if direction == 'север':
            y += steps
        elif direction == 'восток':
            x += steps
        elif direction == 'юг':
            y -= steps
        else:
            x -= steps
    iters += 1
    if x == treasureX and y == treasureY and found == 1:
        print(iters, direction, sep='\n')
        found = 0

    myCommand = input()










