i = int(input()) # rows 2
j = int(input()) # colums 3
table = [[str(input()) for b in range(j)] for a in range(i)]
rev_table = []
for i in range(j):
    rev_table.append([table[l][k] for l in range(i) for k in range(i)])