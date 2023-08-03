from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

students_attendances = []

for i in range(1, number_of_students + 1):
    current_student_attendances = int(input())
    students_attendances.append(current_student_attendances)

if students_attendances:
    best_student = max(students_attendances)
    if number_of_lectures == 0:
        best_student_bonus = 0
    else:
        best_student_bonus = ceil((best_student / number_of_lectures) * (5 + additional_bonus))
else:
    best_student = 0
    best_student_bonus = 0

print(f"Max Bonus: {best_student_bonus}.\nThe student has attended {best_student} lectures.")
