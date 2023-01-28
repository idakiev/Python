# •	Първи ред – начало на интервала – цяло число в интервала [1...999]
# •	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# •	Трети ред – магическото число – цяло число в интервала [1...10000]

start_iteration = int(input())
end_iteration = int(input())
magic_number = int(input())

x1 = 0
x2 = 0

iterations_counter = 0

for i in range(start_iteration, end_iteration + 1):
    x1 = i
    for i2 in range(start_iteration, end_iteration + 1):
        x2 = i2
        if x1 + x2 == magic_number:
            iterations_counter += 1
            print(f"Combination N:{iterations_counter} ({x1} + {x2} = {magic_number})")
            break
        else:
            iterations_counter += 1
    if x1 + x2 == magic_number:
        break
if x1 + x2 != magic_number:
    print(f"{iterations_counter} combinations - neither equals {magic_number}")
