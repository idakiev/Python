budget = int(input())
season = input()
people = int(input())

boat_rent = 0
discount = 0
discount_2 = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer":
    boat_rent = 4200
elif season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if 1 <= people <= 6:
    discount = 9/10
elif 7 <= people <= 11:
    discount = 8.5/10
elif people >= 12:
    discount = 7.5/10

if people % 2 == 0 and season != "Autumn":
    discount_2 = 9.5/10

if discount_2 == 0:
    total_amount = boat_rent * discount
else:
    total_amount = (boat_rent * discount)*discount_2

diff = abs(budget - total_amount)

if budget >= total_amount:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
