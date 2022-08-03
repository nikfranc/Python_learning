jCounter, jMem = 1, 1
for i in range(int(input())):
    jCounter -= 1
    print(i + 1, end='\t')
    if jCounter == 0:
        print('')
        jCounter = jMem + 1
        jMem += 1
