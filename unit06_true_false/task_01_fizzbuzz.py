a = int(input())
b = int(input())
for i in range(a, b + 1):
    str = ''
    if i % 3 == 0:
        str += 'Fizz'
    if i % 5 == 0:
        str += 'Buzz'
    if i % 7 == 0:
        str += 'Vuzz'
    if i % 11 == 0:
        str += 'Guzz'

    if str == '':
        print(i)
    else:
        print(str)
