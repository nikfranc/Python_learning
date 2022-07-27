str = 'Ауууу!'
print(str + '\n' + str)  # почему в print(str, '\n', str) лишний пробел?
# - потому что пробел — это базовый разделитель у функции,
# используй sep= или f-строку для более гибкого управления
print('Hi', 'mate')
print('Hi', 'mate', sep='')
print('Hi', 'mate', sep='---')
print('Hi', 'mate', end='')
print('How r u')
