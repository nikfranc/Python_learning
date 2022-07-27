growth1, growth2, growth3 = int(input()), int(input()), int(input())

if growth1 > growth2 and growth1 > growth3:
    if growth2 > growth3:
        print(growth1, growth2, growth3)
    else:
        print(growth1, growth3, growth2)
elif growth2 > growth3:
    if growth3 > growth1:
        print(growth2, growth3, growth1)
    else:
        print(growth2, growth1, growth3)
else:
    if growth2 > growth1:
        print(growth3, growth2, growth1)
    else:
        print(growth3, growth1, growth2)
