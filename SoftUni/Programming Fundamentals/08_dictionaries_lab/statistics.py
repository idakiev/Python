
storage = {}
command = input()

while command != "statistics":
    command = command.split(": ")
    key = command[0]
    value = command[1]
    if key in storage:
        storage[key] = storage[key] + int(value)
    else:
        storage[key] = int(value)
    command = input()

print(f"Products in stock:")
[print(f"- {product}: {quantity}") for (product, quantity) in storage.items()]

# for (key, value) in storage.items():
#     print(f"- {key}: {value}")

print(f"Total Products: {len(storage.keys())}")
print(f"Total Quantity: {sum(storage.values())}")
