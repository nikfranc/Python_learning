print(dict.fromkeys(list((set(list({i: '' for i in str(input()).split()}.keys()))
                          - set(list({i: '' for i in str(input()).split()}.keys())))), ''))