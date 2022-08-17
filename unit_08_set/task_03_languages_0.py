eng_num = int(input())
ger_num = int(input())
eng_set = set()
ger_set = set()

for i in range(eng_num):
    eng_set.add(input())

for i in range(ger_num):
    ger_set.add(input())

if len(eng_set ^ ger_set) > 0:
    print(len(eng_set ^ ger_set))
else:
    print('NO')

