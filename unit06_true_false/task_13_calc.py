while True:
    firstNum = int(input())
    operation = input()

    if operation == '!':
        fact = 1
        for i in range(2, firstNum + 1):
            fact *= i
        print(fact)
        continue
    elif operation == 'x':
        print(firstNum)
        break

    secondNum = int(input())

    if operation == '+':
        print(firstNum + secondNum)
    elif operation == '-':
        print(firstNum - secondNum)
    elif operation == '*':
        print(firstNum * secondNum)
    elif operation == '/':
        if secondNum != 0:
            print(firstNum - secondNum)
        else:
            continue
    elif operation == '%':
        print(firstNum % secondNum)

