requests_list = list()
for i in range(int(input())):
    requests_list.append(str(input()))
search_query = str(input())
for request in requests_list:
    if search_query in request:
        print(request)