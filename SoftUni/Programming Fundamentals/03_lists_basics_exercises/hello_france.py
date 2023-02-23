items = input().split("|")
budget = float(input())
profit = 0
bought_items = list()

for i in range(len(items)):
    current_element = items[i].split("->")
    if budget >= float(current_element[1]):
        if current_element[0] == "Clothes":
            if float(current_element[1]) <= 50:
                budget -= float(current_element[1])
                profit += float(current_element[1]) * 0.4
                bought_items.append(float(current_element[1]) * 1.4)
            else:
                continue
        if current_element[0] == "Shoes":
            if float(current_element[1]) <= 35:
                budget -= float(current_element[1])
                profit += float(current_element[1]) * 0.4
                bought_items.append(float(current_element[1]) * 1.4)
            else:
                continue
        if current_element[0] == "Accessories":
            if float(current_element[1]) <= 20.5:
                budget -= float(current_element[1])
                profit += float(current_element[1]) * 0.4
                bought_items.append(float(current_element[1]) * 1.4)
            else:
                continue
    else:
        continue

for items in range(len(bought_items)):
    print(f"{bought_items[items]:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

if (sum(bought_items) + budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
