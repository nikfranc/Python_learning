curr_word = str(input())
short_word = curr_word
long_word = ''
while curr_word != 'стоп':
    if len(short_word) > len(curr_word):
        short_word = curr_word
    elif len(long_word) < len(curr_word):
        long_word = curr_word
    curr_word = str(input())

short_set = set(short_word)
long_set = set(long_word)

if short_set <= long_set:
    print('ДА')
else:
    print('НЕТ')
