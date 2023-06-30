
number_of_commands = int(input())

students_grades = {}

for _ in range(1, number_of_commands + 1):
    current_student = input()
    current_grade = float(input())
    if current_student not in students_grades:
        students_grades[current_student] = [current_grade]
    else:
        students_grades[current_student].append(current_grade)

for key, value in students_grades.items():
    avg_grade = sum(value) / len(value)
    if avg_grade >= 4.50:
        print(f"{key} -> {avg_grade:.2f}")
