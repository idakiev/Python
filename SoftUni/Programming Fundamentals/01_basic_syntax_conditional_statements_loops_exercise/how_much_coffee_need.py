command = input()

number_of_coffee = 0

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        number_of_coffee += 1
        command = input()
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        number_of_coffee += 2
        command = input()
    else:
        command = input()

if number_of_coffee > 5:
    print("You need extra sleep")
else:
    print(number_of_coffee)
