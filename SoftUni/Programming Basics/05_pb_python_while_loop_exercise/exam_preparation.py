max_bad_grade = int(input())


grades_counter = 0
bad_grade_counter = 0
exam_counter = 0
last_exam = ""

while True:
    exam_name = input()

    exam_counter += 1
    if exam_name != "Enough":
        exam_grade = int(input())
        last_exam = exam_name
        grades_counter += exam_grade

        if exam_grade <= 4:
            bad_grade_counter += 1
            if bad_grade_counter == max_bad_grade:
                print(f"You need a break, {max_bad_grade} poor grades.")
                break
    else:
        exam_counter -= 1
        avg_grade = grades_counter / exam_counter
        print(f"Average score: {avg_grade:.2f}")
        print(f"Number of problems: {exam_counter}")
        print(f"Last problem: {last_exam}")
        break
