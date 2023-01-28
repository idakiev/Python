destination = input()

money_saved = 0

while destination != "End":
    money_needed = float(input())
    money_saved = float(input())
    while money_needed > money_saved:
        money_saved += float(input())
    else:
        print(f"Going to {destination}!")
        destination = input()
