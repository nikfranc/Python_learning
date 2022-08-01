currPrice = int(input())
prevPrice = currPrice
bought = False
while currPrice != 0:
    if currPrice > prevPrice and not bought:
        boughtPrice = currPrice
        bought = True
    elif currPrice < prevPrice and bought:
        sellPrice = currPrice
    prevPrice = currPrice
    currPrice = int(input())
print(boughtPrice, sellPrice, sellPrice - boughtPrice)


