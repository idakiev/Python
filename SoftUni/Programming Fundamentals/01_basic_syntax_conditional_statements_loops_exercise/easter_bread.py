
budget = float(input())
flour_price_per_kg = float(input())

eggs_price = flour_price_per_kg * 0.75
milk_price_per_litre = flour_price_per_kg * 1.25

loaf_price = flour_price_per_kg + eggs_price + (milk_price_per_litre * 0.25)

loaf_count = 0
colored_eggs = 0

while loaf_price < budget:
    budget -= loaf_price
    loaf_count += 1
    colored_eggs += 3
    if loaf_count % 3 == 0:
        colored_eggs -= loaf_count - 2

print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
