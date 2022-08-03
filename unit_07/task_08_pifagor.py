num = int(input())
for m in range(1, num + 1):
    for n in range(1, num + 1):
        if m ** 2 > n ** 2 and m ** 2 + n ** 2 <= num:
            x = m ** 2 - n ** 2
            y = 2 * m * n
            z = m ** 2 + n ** 2
            no_divider = True
            for i in range(2, min(x, y, z) // 2 + 1):
                if x % i == 0 and y % i == 0 and z % i == 0:
                    no_divider = False
            if no_divider:
                print(min(x, y), max(x, y), z)
            else:
                continue
