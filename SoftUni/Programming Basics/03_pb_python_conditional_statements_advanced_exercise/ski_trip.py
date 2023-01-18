days_number = int(input())
room_type = input()
feedback = input()

room_for_one = 18
apartment = 25
president_apartment = 35

price = 0
nights = days_number - 1


if days_number < 10:
    if room_type == "room for one person":
        price = room_for_one
    if room_type == "apartment":
        price = apartment * 0.70
    if room_type == "president apartment":
        price = president_apartment * 0.90

if 10 <= days_number <= 15:
    if room_type == "room for one person":
        price = room_for_one
    if room_type == "apartment":
        price = apartment * 0.65
    if room_type == "president apartment":
        price = president_apartment * 0.85

if days_number > 15:
    if room_type == "room for one person":
        price = room_for_one
    if room_type == "apartment":
        price = apartment * 0.50
    if room_type == "president apartment":
        price = president_apartment * 0.80

if feedback == "positive":
    price = price + (price * 0.25)
else:
    price = price - (price * 0.10)

total_amount = nights * price

print(f"{total_amount:.2f}")
