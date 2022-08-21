prev_town = str(input())
curr_town = str(input())
while curr_town[-1] == prev_town[0]:
    prev_town = curr_town
    curr_town = str(input())
print(curr_town)
