import re

data = input()

search_pattern = r"([\#|\|])([A-Za-z\s]+)\1([0-9]{2}[\/][0-9]{2}[\/][0-9]{2})\1([0-9]{1,5})\1"

valid_results = re.findall(search_pattern, data)

calories_per_day = 2000
products = []
total_calories = 0

for symbol, product, exp_date, calories in valid_results:
    products.append([product, exp_date, calories])
    total_calories += int(calories)

days_to_last = total_calories // calories_per_day

print(f"You have food to last you for: {days_to_last} days!")

for i in products:
    current_product = i[0]
    current_exp_date = i[1]
    current_calories = i[2]
    print(f"Item: {current_product}, Best before: {current_exp_date}, Nutrition: {current_calories}")
