growth1 = input()
growth2 = input()
growth3 = input()
growth = [growth1, growth2, growth3]
f = 0
while f == 0:
    f = 1
    for i in range(2):
        if growth[i] > growth[i + 1]:
            growth[i], growth[i + 1] = growth[i + 1], growth[i]
            swapped = 0
print(growth)