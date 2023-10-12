from collections import deque

cups = deque(int(x) for x in input().split(" "))
bottles = [int(x) for x in input().split(" ")]

wasted_water = 0

while bottles:
    if cups:
        current_bottle = bottles.pop()
        current_cup = cups[0]
        if current_bottle >= current_cup:
            wasted_water += current_bottle - current_cup
            cups.popleft()
        else:
            cups[0] -= current_bottle
    else:
        print(f"Bottles: {' '.join(str(x) for x in bottles)}")
        print(f"Wasted litters of water: {wasted_water}")
        raise SystemExit

if cups:
    print(f"Cups: {' '.join(str(x) for x in cups)}")
    print(f"Wasted litters of water: {wasted_water}")
