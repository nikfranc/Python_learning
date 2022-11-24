def bracket_check(my_str):
    while my_str:
        if my_str[0] == '(':
            str_list = list(my_str)
            if ')' in str_list:
                str_list.pop(0)
                str_list.remove(')')
                my_str = ''.join(str_list)
            else:
                print('NO')
                exit(0)
        else:
            print('NO')
            exit(0)
    print('YES')


bracket_check('(()(()')

