num_count = int(input())

left_sum = 0

for _ in range(1, num_count + 1):
    left_sum += int(input())

right_sum = 0

for _ in range(1, num_count + 1):
    right_sum += int(input())

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")

