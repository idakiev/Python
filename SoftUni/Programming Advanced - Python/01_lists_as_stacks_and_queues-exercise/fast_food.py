from collections import deque

food_stock = int(input())

orders = deque(map(int, input().split(" ")))

biggest_order = max(map(int, orders))

print(biggest_order)

while food_stock > 0 and orders:
    current_order = orders[0]
    if current_order <= food_stock:
        food_stock -= current_order
        orders.popleft()

    else:
        break

if not orders:
    print("Orders complete")
else:
    print(f"Orders left: ", end="")
    print(*orders)
