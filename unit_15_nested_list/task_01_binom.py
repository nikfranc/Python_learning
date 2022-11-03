n = int(input())
binom = [[0] * 10 for _ in range(10)]
for i in range(n):
    binom[i][0] = 1
    for j in range(1, n):
        binom[i][j] = binom[i-1][j-1] + binom[i-1][j]
for i in range(n):
    for j in range(n):
        if binom[i][j] > 0:
            print(binom[i][j], end=' ')
    print('')
