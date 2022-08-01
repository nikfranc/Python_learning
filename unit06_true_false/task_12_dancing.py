patience = int(input())
correctCount = 0
countNum = 1
while patience != 0:
    count = input()
    if countNum == 4:
        countNum = 1
    if (count != 'раз' and countNum == 1) or (count != 'два' and countNum == 2) or (count != 'три' and countNum == 3):
        patience -= 1
        if patience == 0:
            print('На сегодня хватит.')
        else:
            print('Правильных отсчетов было ', correctCount, ' ,но теперь вы ошиблись.')
            correctCount = 0
    else:
        correctCount += 1

    countNum += 1


