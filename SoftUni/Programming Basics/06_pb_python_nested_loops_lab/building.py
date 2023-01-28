floors = int(input())
units = int(input())

app_type = ""
top_floor = floors

for levels in range(floors, 0, -1):
    if levels % 2 != 0:
        app_type = "A"
    else:
        app_type = "O"
    if top_floor == levels:
        app_type = "L"

    for apartments in range(0, units):

        print(f"{app_type}{levels}{apartments}", end=" ")
    print()
