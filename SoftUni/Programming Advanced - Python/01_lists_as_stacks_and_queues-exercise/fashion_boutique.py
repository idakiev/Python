
clothes_stack = [int(x) for x in input().split(" ")]

rack_capacity = int(input())

rack_capacity_copy = rack_capacity
rack_counter = 1

while clothes_stack:
    current_clothes = clothes_stack[-1]

    if rack_capacity_copy - current_clothes < 0:
        rack_counter += 1
        rack_capacity_copy = rack_capacity
        continue
    else:
        rack_capacity_copy -= current_clothes
        clothes_stack.pop()

    if clothes_stack:
        current_clothes = clothes_stack[-1]
    else:
        break

print(rack_counter)
