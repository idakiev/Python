
longest_intersection = []

for i in range(int(input())):
    command = input().split("-")

    first_range = command[0].split(",")
    second_range = command[1].split(",")

    first_numbers = set(x for x in range(int(first_range[0]), int(first_range[1]) + 1))
    second_numbers = set(x for x in range(int(second_range[0]), int(second_range[1]) + 1))
    intersection = first_numbers.intersection(second_numbers)

    if len(intersection) > len(longest_intersection):
        longest_intersection = [x for x in intersection]

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
