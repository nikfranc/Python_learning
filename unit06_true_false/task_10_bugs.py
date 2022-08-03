squareSide = float(input())
bugSpeed = float(input())
distance = squareSide
seconds = 0
if distance != bugSpeed:
    while distance - bugSpeed > 0:
        firstSide = distance - bugSpeed
        secondSide = bugSpeed
        distance = round((firstSide ** 2 + secondSide ** 2) ** 0.5, 2)
        seconds += 1
    print(seconds)
else:
    print(1)
