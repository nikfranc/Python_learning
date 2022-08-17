fridge_num = int(input())
fridge_set = set()
for i in range(fridge_num):
    fridge_set.add(input())

recipe_num = int(input())
can_cook_set = set()
recipe_list = set()

for i in range(recipe_num):
    curr_recipe = input()
    ingrid_num = int(input())
    for j in range(ingrid_num):
        recipe_list.add(input())
    if recipe_list & fridge_set == recipe_list:
        can_cook_set.add(curr_recipe)

print(*can_cook_set, sep='\n')
