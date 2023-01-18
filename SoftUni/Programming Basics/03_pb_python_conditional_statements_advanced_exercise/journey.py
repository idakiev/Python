budget = float(input())
season = input()

cost = 0

if season == "summer":
    accommodation = "Camp"
    if 0 < budget <= 100:
        destination = "Bulgaria"
        cost = budget * 0.30
    if 100 < budget <= 1000:
        destination = "Balkans"
        cost = budget * 0.40
    if budget > 1000:
        accommodation = "Hotel"
        destination = "Europe"
        cost = budget * 0.90

if season == "winter":
    accommodation = "Hotel"
    if 0 < budget <= 100:
        destination = "Bulgaria"
        cost = budget * 0.70
    if 100 < budget <= 1000:
        destination = "Balkans"
        cost = budget * 0.80
    if budget > 1000:
        destination = "Europe"
        cost = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{accommodation} - {cost:.2f}")
