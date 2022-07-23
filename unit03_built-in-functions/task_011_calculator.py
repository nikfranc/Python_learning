num1 = float(input())
num2 = float(input())
oper = input()
operators = ['+', '-', '*', '/']
if (num2 == 0 and oper == '/') or oper not in operators:
    print(888888)
else:
    if(oper == '+'):
        print(num1 + num2)
    elif (oper == '-'):
        print(num1 - num2)
    elif (oper == '*'):
        print(num1 * num2)
    else:
        print(num1 / num2)

