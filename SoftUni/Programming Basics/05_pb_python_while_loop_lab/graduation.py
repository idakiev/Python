student_name = input()

year_counter = 0
grade_counter = 0
years_failed = 0

while True:
    current_year_grade = float(input())

    if current_year_grade >= 4:
        grade_counter += current_year_grade
        year_counter += 1
    else:
        years_failed += 1

    if years_failed > 1 or year_counter == 12:

        break



if years_failed > 1:
    year_counter += 1
    print(f"{student_name} has been excluded at {year_counter} grade")
else:
    avg_grade = grade_counter / year_counter
    print(f"{student_name} graduated. Average grade: {avg_grade:.2f}")
