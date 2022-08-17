paper_num = int(input())
active_paper = set()
new_paper = set()
for i in range(paper_num):
    stud_num = int(input())
    active_paper.clear()
    for j in range(stud_num):
        active_paper.add(input())
    if i == 0:
        new_paper = active_paper
    else:
        new_paper = new_paper & active_paper
print(*new_paper, sep='\n')


