month = input()
nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < nights <= 14:
        studio = studio * 0.95
    elif nights > 14:
        studio = studio * 0.70

if month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio = studio * 0.80

if month == "July" or month == "August":
    studio = 76
    apartment = 77

if nights > 14:
    apartment = apartment * 0.90

total_studio = f"{(nights * studio):.2f}"
total_apartment = f"{(nights * apartment):.2f}"

print(f"Apartment: {total_apartment} lv.")
print(f"Studio: {total_studio} lv.")
