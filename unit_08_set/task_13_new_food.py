dish_num = int(input())
all_dishes = set()

for i in range(dish_num):
    all_dishes.add(input())

days = int(input())
curr_dishes = set()

for i in range(days):
    dish_num = int(input())
    for j in range(dish_num):
        curr_dishes.add(input())
    all_dishes = all_dishes - curr_dishes


print(*all_dishes, sep='\n')
