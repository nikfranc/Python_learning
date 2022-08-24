first_word = str(input())
second_word = str(input())
bulls = 0
cows = 0
for i in range(len(first_word)):
    if first_word[i] == second_word[i]:
        bulls += 1
    elif first_word[i] in second_word:
        cows += 1
print(cows, bulls, sep='\n')
