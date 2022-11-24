def equation(m, n):
    m = list(map(float, m.split(';')))
    n = list(map(float, n.split(';')))
    print(m)
    print(n)
    k = -(n[1] - m[1]) / (m[0] - n[1])
    b = -(n[0] * m[1] - m[0] * n[1]) / (m[0] - n[0])
    if k != 0:
        print(k, b)
    else:
        print(b)


equation("0;0", "1;1")