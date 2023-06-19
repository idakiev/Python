
countries = input().split(", ")
capitals = input().split(", ")

for i, k in zip(countries, capitals):
    print(f"{i} -> {k}")
