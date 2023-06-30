
command = input()

products = {}

while command != "buy":
    command = command.split(" ")
    key = command[0]
    value_price = float(command[1])
    value_quantity = int(command[2])
    if key not in products.keys():
        products[key] = {'price': value_price, 'quantity': value_quantity}
    else:
        if products[key]['price'] != value_price:
            products[key]['price'] = value_price
            products[key]['quantity'] += value_quantity
        else:
            products[key]['quantity'] += value_quantity

    command = input()

for key, value in products.items():
    result_value = products[key]['price'] * products[key]['quantity']
    print(f"{key} -> {result_value:.2f}")
