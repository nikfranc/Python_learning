num = int(input())

n1 = num // 1000
n2 = (num - n1 * 1000) // 100
n3 = (num - n1 * 1000 - n2 * 100) // 10
n4 = num - n1 * 1000 - n2 * 100 - n3 * 10

if n1 > n2:
    n1, n2 = n2, n1
if n1 > n3:
    n1, n3 = n3, n1
if n1 > n4:
    n1, n4 = n4, n1
if n2 > n3:
    n2, n3 = n3, n2
if n2 > n4:
    n2, n4 = n4, n2
if n3 > n4:
    n3, n4 = n4, n3

print(n1, n2, n3, n4, sep = '')