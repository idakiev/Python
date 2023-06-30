
shadowmourne_item = 250  # "Shadowmourne" - requires 250 Shards #
is_shadowmourne = False

valanyr_item = 250  # "Valanyr" - requires 250 Fragments #
is_valanyr = False

dragonwrath = 250  # "Dragonwrath" - requires 250 Motes #
is_dragonwrath = False

materials_collected = {"shards": 0, "fragments": 0, "motes": 0}

while not is_shadowmourne and not is_valanyr and not is_dragonwrath:
    command = input().lower().split(" ")
    key_list = []
    value_list = []
    for i in range(len(command)):
        if i % 2 != 0:
            key_list.append(command[i])
        else:
            value_list.append(command[i])
    for key, value in zip(key_list, value_list):
        if key not in materials_collected:
            materials_collected[key] = int(value)
        else:
            materials_collected[key] += int(value)

        if materials_collected["shards"] >= 250:
            materials_collected["shards"] -= 250
            is_shadowmourne = True
            break

        if materials_collected["fragments"] >= 250:
            materials_collected["fragments"] -= 250
            is_valanyr = True
            break

        if materials_collected["motes"] >= 250:
            materials_collected["motes"] -= 250
            is_dragonwrath = True
            break

if is_shadowmourne:
    print(f"Shadowmourne obtained!")
if is_valanyr:
    print(f"Valanyr obtained!")
if is_dragonwrath:
    print(f"Dragonwrath obtained!")

if "shards" in materials_collected.keys():
    value = materials_collected["shards"]
    print(f"shards: {value}")
if "fragments" in materials_collected.keys():
    value = materials_collected["fragments"]
    print(f"fragments: {value}")
if "motes" in materials_collected.keys():
    value = materials_collected["motes"]
    print(f"motes: {value}")

for key, value in materials_collected.items():
    if key != "shards" and key != "fragments" and key != "motes":
        print(f"{key}: {value}")
