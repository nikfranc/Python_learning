levels = int(input())
for i in range(1, levels + 1):
    print((levels - i) * ' ', (2 * i - 1) * '*', sep='')
