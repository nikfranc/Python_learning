notebook_str = [str(input()) for i in range(int(input()))]
print(', '.join([i for i in notebook_str if "лук" not in i]))
