dict1 = {i: '' for i in str(input()).split()}
dict2 = {i: '' for i in str(input()).split()}
print(dict.fromkeys(list((set(list(dict1.keys()))) | (set(list(dict2.keys())) - set(list(dict1.keys()))))))
