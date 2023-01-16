hours = int(input())
minutes = int(input())

total_minutes = minutes + 15

if total_minutes > 59:
    hours = hours + 1
    total_minutes = total_minutes - 60

if hours > 23:
    hours = 0

if total_minutes < 9:
    print(f"{hours}:0{total_minutes}")
else:
    print(f"{hours}:{total_minutes}")
