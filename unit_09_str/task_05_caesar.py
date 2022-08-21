gap = int(input())
message = str(input())
new_message = ''

alph_up = ''
alph_low = ''
for i in range(ord('А'), ord('Я') + 1):
    alph_up += chr(i)
for i in range(ord('а'), ord('я') + 1):
    alph_low += chr(i)

for i in range(len(message)):
    if message[i] in alph_low:
        curr_index = alph_low.find(message[i])
        if curr_index + gap > alph_low.find('я'):
            new_message += alph_low[gap - (len(alph_low) - curr_index)]
        else:
            new_message += alph_low[curr_index + gap]
    elif message[i] in alph_up:
        curr_index = alph_up.find(message[i])
        if curr_index + gap > alph_up.find('Я'):
            new_message += alph_up[gap - (len(alph_low) - curr_index)]
        else:
            new_message += alph_up[curr_index + gap]
    else:
        new_message += message[i]
print(new_message)


