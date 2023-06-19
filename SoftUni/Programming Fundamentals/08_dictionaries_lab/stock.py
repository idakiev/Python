
products = input().split(" ")
storage = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i+1]
    storage[key] = int(value)

products_to_check = input().split(" ")

for k in products_to_check:
    current_product = k
    if k in storage:
        quantity = storage[k]
        print(f"We have {quantity} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
