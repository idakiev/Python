
values = input().split(" ")

values_tuple = tuple(float(x) for x in values)

checked_values = []

for i in values_tuple:
    if i not in checked_values:
        print(f"{i:.1f} - {values_tuple.count(i)} times")
        checked_values.append(i)
