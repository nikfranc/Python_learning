treasureX = int(input())
treasureY = int(input())
myCommand = input()
iters = 0
found = False
x = 0
y = 0
while myCommand != 'стоп':
    if myCommand == 'север':
         steps = int(input())
         y += steps
    elif myCommand == 'юг':
        steps = int(input())
        y -= steps
    elif myCommand == 'запад':
        steps = int(input())
        x -= steps
    else:
        steps = int(input())
        x += steps
    iters += 1

    if x == treasureX and y == treasureY and not found:
        print(iters)
        found = True

    myCommand = input()








