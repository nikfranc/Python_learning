currPrice = float(input())
sum = 0
while currPrice > 0:
    if currPrice > 1000:
        currPrice *= 0.95
    sum += currPrice
    currPrice = float(input())
print(sum)
