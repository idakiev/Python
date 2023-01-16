city = input()
sales = float(input())

total = 0

if sales < 0:
    print("error")

if 0 <= sales <= 500:
    if city == "Sofia":
        total = sales * 0.05
        print(f"{total:.2f}")
    elif city == "Varna":
        total = sales * 0.045
        print(f"{total:.2f}")
    elif city == "Plovdiv":
        total = sales * 0.055
        print(f"{total:.2f}")
    else:
        print("error")

elif 500 < sales <= 1000:
    if city == "Sofia":
        total = sales * 0.07
        print(f"{total:.2f}")
    elif city == "Varna":
        total = sales * 0.075
        print(f"{total:.2f}")
    elif city == "Plovdiv":
        total = sales * 0.08
        print(f"{total:.2f}")
    else:
        print("error")

elif 1000 < sales <= 10000:
    if city == "Sofia":
        total = sales * 0.08
        print(f"{total:.2f}")
    elif city == "Varna":
        total = sales * 0.10
        print(f"{total:.2f}")
    elif city == "Plovdiv":
        total = sales * 0.12
        print(f"{total:.2f}")
    else:
        print("error")

elif sales > 10000:
    if city == "Sofia":
        total = sales * 0.12
        print(f"{total:.2f}")
    elif city == "Varna":
        total = sales * 0.13
        print(f"{total:.2f}")
    elif city == "Plovdiv":
        total = sales * 0.145
        print(f"{total:.2f}")
    else:
        print("error")
