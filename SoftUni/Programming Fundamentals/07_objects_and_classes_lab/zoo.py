
class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        if species == "fish":
            self.fishes.append(name)
        if species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            print(f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}")
        if species == "fish":
            print(f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)}")
        if species == "bird":
            print(f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}")
        return f"Total animals: {Zoo.__animals}"


zoo_name = Zoo(input())

command_count = int(input())

for i in range(command_count):
    current_command = input().split(" ")
    Zoo.add_animal(zoo_name, current_command[0], current_command[1])

final_command = input()

print(Zoo.get_info(zoo_name, final_command))
