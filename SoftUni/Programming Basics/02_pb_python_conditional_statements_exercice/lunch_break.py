import math

series_name = input()
episode_minutes = int(input())
lunch_break = int(input())

lunch_time = lunch_break / 8
relax_time = lunch_break / 4

time_needed = episode_minutes + lunch_time + relax_time
difference = abs(time_needed - lunch_break)

if time_needed <= lunch_break:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(difference)} more minutes.")
