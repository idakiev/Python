import time
# from collections import deque

start_time = time.time()

numbers = list(int(x) for x in input().split(" "))

target_number = int(input())

while numbers:
    current_number = numbers[0]
    numbers.pop(0)
    for i in range(len(numbers)):
        if current_number + numbers[i] == target_number:
            print(f"{current_number} + {numbers[i]} = {target_number}")
            numbers.pop(i)
            break
        else:
            continue

# print("--- %s seconds ---" % (time.time() - start_time))
end = time.time()
print(f"Time range: {end-start_time}")
