
import math

world_record = float(input())
total_distance = float(input())
seconds_per_m = float(input())

delay = math.floor(total_distance / 15) * 12.5
new_time = (total_distance * seconds_per_m) + delay
difference = abs(new_time - world_record)

if new_time >= world_record:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
