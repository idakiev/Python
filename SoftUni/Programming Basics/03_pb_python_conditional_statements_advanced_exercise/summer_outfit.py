temperature = int(input())
time_of_day = input()

outfit = "outfit"
shoes = "shoes"

if time_of_day == "Morning":
    if 10 <= temperature <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    if 18 < temperature <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    if temperature >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"

if time_of_day == "Afternoon":
    if 10 <= temperature <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if 18 < temperature <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    if temperature >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"

if time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
