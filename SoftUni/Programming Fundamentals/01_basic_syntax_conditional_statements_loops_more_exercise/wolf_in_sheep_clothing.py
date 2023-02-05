
animals = input()

current_animal = ""

list_from_animals = []

for i in range(len(animals)):
    if animals[i] != "," and animals[i] != " ":
        current_animal += animals[i]
    if current_animal == "sheep":
        list_from_animals.append("sheep")
        current_animal = ""
    if current_animal == "wolf":
        list_from_animals.append("wolf")
        current_animal = ""

if list_from_animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    list_from_animals_reversed = list(reversed(list_from_animals))
    wolf_index = list_from_animals_reversed.index("wolf")
    print(f"Oi! Sheep number {wolf_index}! You are about to be eaten by a wolf!")
