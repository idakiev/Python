
vip_guests = set()
other_guests = set()

for i in range(int(input())):
    command = input()
    if command[0].isdigit():
        vip_guests.add(command)
    else:
        other_guests.add(command)

command = input()

while command != "END":
    if command[0].isdigit() and command in vip_guests:
        vip_guests.remove(command)
    elif command[0].isalpha() and command in other_guests:
        other_guests.remove(command)

    command = input()

guests_left = len(vip_guests) + len(other_guests)

print(guests_left)

if vip_guests:
    for vip in sorted(vip_guests):
        print(vip)

if other_guests:
    for other in sorted(other_guests):
        print(other)
