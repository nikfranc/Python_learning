student_num = int(input()) + int(input()) + int(input())
student_set_1 = set()
student_set_2 = set()

for i in range(student_num):
    curr_student = input()
    if curr_student in student_set_1:
        if curr_student not in student_set_2:
            student_set_2.add(curr_student)
            continue
        else:
            student_set_2.discard(curr_student)
    else:
        student_set_1.add(curr_student)

print(len(student_set_2))
