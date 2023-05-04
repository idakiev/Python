employees = list(map(int, input().split(" ")))
improvement_factor = int(input())

employees_happiness = [x*improvement_factor for x in employees]
average_happiness = sum(employees_happiness) / len(employees)

employees_above_avg = list(filter(lambda y: y > average_happiness, employees_happiness))

if len(employees_above_avg) >= (len(employees) / 2):
    print(f"Score: {len(employees_above_avg)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(employees_above_avg)}/{len(employees)}. Employees are not happy!")
