numbers = input()

initial_list = numbers.split(" ")

opposite_list = []

for k in initial_list:
    opposite_list.append(-int(k))

print(opposite_list)
