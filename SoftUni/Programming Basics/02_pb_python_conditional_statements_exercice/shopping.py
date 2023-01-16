
budget = float(input())

vga_number = int(input())
cpu_number = int(input())
ram_number = int(input())

vga_price = vga_number * 250
cpu_price = cpu_number * (vga_price * 0.35)
ram_price = ram_number * (vga_price * 0.10)

total_price = vga_price + cpu_price + ram_price


if vga_number > cpu_number:
    total_price = total_price * 0.85

difference = abs(total_price - budget)

if total_price <= budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
