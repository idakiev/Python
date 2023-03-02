car_track = input().split(" ")

left_racer_time = 0
right_racer_time = 0

mid_of_track = len(car_track) // 2

for left in range(mid_of_track):
    current_time = int(car_track[left])
    if 0 < current_time != 0:
        left_racer_time += current_time
    else:
        left_racer_time = left_racer_time * 0.8

for right in reversed(range(mid_of_track + 1, len(car_track))):
    current_time = int(car_track[right])
    if 0 < current_time != 0:
        right_racer_time += current_time
    else:
        right_racer_time = right_racer_time * 0.8

if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
