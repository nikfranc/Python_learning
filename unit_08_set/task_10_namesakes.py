people_num = int(input())
people_set = set()
namesakes_set = set()
same_count = 0
for i in range(people_num):
    curr_dude = input()
    if curr_dude in people_set:
        same_count += 1
        namesakes_set.add(curr_dude)
    else:
        people_set.add(curr_dude)
print(len(namesakes_set) + same_count)