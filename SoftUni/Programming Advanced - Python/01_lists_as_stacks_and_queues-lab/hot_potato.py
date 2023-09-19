
from collections import deque

kids_names = deque(input().split())

hot_potato = int(input())

while len(kids_names) != 1:
    for i in range(1, hot_potato + 1):
        if i != hot_potato:
            removed = kids_names.popleft()
            kids_names.append(removed)
        else:
            print(f"Removed {kids_names.popleft()}")

print(f"Last is {kids_names.popleft()}")
