hour = int(input())
day = input()

status = "open"

if 10 <= hour <= 18:
    if day == "Monday":
        status = "open"
    elif day == "Tuesday":
        status = "open"
    elif day == "Wednesday":
        status = "open"
    elif day == "Thursday":
        status = "open"
    elif day == "Friday":
        status = "open"
    elif day == "Saturday":
        status = "open"
    elif day == "Sunday":
        status = "closed"
else:
    status = "closed"

print(status)
