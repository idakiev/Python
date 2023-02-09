
n = int(input())

tank_capacity = 255
current_capacity = 0

for i in range(n):
    current_litres = int(input())
    current_capacity += current_litres
    if current_capacity > tank_capacity:
        current_capacity -= current_litres
        print("Insufficient capacity!")
        continue
    else:
        continue

print(current_capacity)
