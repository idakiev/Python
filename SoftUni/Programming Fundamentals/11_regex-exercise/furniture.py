import re

command = input()
furniture_bought = []
total_money = 0

while command != "Purchase":
    search_pattern = r">>([a-zA-Z]+)<<([0-9]+[\.]*[0-9]*)!([0-9]+)"
    result = re.search(search_pattern, command)
    if result:
        furniture, price, quantity = result.groups()
        furniture_bought.append(furniture)
        total_money += float(price) * int(quantity)

    command = input()

print("Bought furniture:")
if furniture_bought:
    print('\n'.join(furniture_bought))
print(f"Total money spend: {total_money:.2f}")
