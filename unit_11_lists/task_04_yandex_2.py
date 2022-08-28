requests_list = list()
for i in range(int(input())):
    requests_list.append(str(input()))

query_list = list()
for i in range(int(input())):
    query_list.append(str(input()))

for request in requests_list:
    str_found = True
    for query in query_list:
        if query not in request:
            str_found = False
    if str_found:
        print(request)
