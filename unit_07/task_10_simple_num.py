num = int(input())
for i in range(1, num):
    is_prime = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i)
