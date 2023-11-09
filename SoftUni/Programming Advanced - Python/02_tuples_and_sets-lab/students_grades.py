
number_of_students = int(input())

students_dict = {}

for i in range(number_of_students):
    command = tuple(input().split())
    student_name, student_grade = command

    if student_name not in students_dict:
        students_dict[student_name] = [float(student_grade)]
    else:
        students_dict[student_name].append(float(student_grade))

for student, grades in students_dict.items():
    avg_grade = sum(float(x) for x in grades) / len(grades)
    if avg_grade < 2:
        avg_grade = 2.00
    print(f"{student} -> {' '.join(str(f'{x:.2f}') for x in grades)} (avg: {avg_grade:.2f})")
