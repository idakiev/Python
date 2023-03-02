numbers = input().split(" ")

command = input().split(" ")

while command[0] != "end":
    if "exchange" in command:
        if 0 <= int(command[1]) < len(numbers):
            current_list_left = numbers[:int(command[1]) + 1]
            current_list_right = numbers[int(command[1]) + 1:]
            numbers = current_list_right + current_list_left

        else:
            print("Invalid index")
            # numbers_int = list(map(int, numbers))
            # print(f"{numbers_int}")

    # searching for MAX even/odd element; returns INDEX
    if "max" in command:
        if command[1] == "even":
            is_even_found = False
            numbers_even = []
            for i in range(len(numbers)):
                if int(numbers[i]) % 2 == 0:
                    numbers_even.append(numbers[i])
                else:
                    continue
            if numbers_even:
                max_even = max(map(int, numbers_even))
                for k in range(len(numbers) - 1, - 1, -1):
                    if int(numbers[k]) == int(max_even):
                        print(f"{k}")
                        is_even_found = True
                        break
                    else:
                        continue
            if not is_even_found:
                print("No matches")

        if command[1] == "odd":
            is_odd_found = False
            numbers_odd = []

            for i in range(len(numbers)):
                if int(numbers[i]) % 2 != 0:
                    numbers_odd.append(numbers[i])
                else:
                    continue
            if numbers_odd:
                max_odd = max(map(int, numbers_odd))
                for k in range(len(numbers) - 1, - 1, -1):
                    if int(numbers[k]) == int(max_odd):
                        print(f"{k}")
                        is_odd_found = True
                        break
                    else:
                        continue
            if not is_odd_found:
                print("No matches")

    # searching for MIN even/odd element; returns INDEX
    if "min" in command:
        if command[1] == "even":
            is_even_found = False
            numbers_even = []

            for i in range(len(numbers)):
                if int(numbers[i]) % 2 == 0:
                    numbers_even.append(numbers[i])
                else:
                    continue
            if numbers_even:
                min_even = min(map(int, numbers_even))
                for k in range(len(numbers) - 1, - 1, -1):
                    if int(numbers[k]) == int(min_even):
                        print(f"{k}")
                        is_even_found = True
                        break
                    else:
                        continue
            if not is_even_found:
                print("No matches")

        if command[1] == "odd":
            is_odd_found = False
            numbers_odd = []
            for i in range(len(numbers)):
                if int(numbers[i]) % 2 != 0:
                    numbers_odd.append(numbers[i])
                else:
                    continue
            if numbers_odd:
                min_odd = min(map(int, numbers_odd))
                for k in range(len(numbers) - 1, - 1, -1):
                    if int(numbers[k]) == int(min_odd):
                        print(f"{k}")
                        is_odd_found = True
                        break
                    else:
                        continue
            if not is_odd_found:
                print("No matches")

    if "first" in command:
        if command[2] == "even":
            if int(command[1]) > len(numbers) or int(command[1]) <= 0:
                print("Invalid count")

            else:
                first_count = []
                for c in range(len(numbers)):
                    if int(numbers[c]) % 2 == 0:
                        first_count.append(numbers[c])
                        if len(first_count) == int(command[1]):
                            break
                        else:
                            continue
                print(list(map(int, first_count)))
        if command[2] == "odd":
            if int(command[1]) > len(numbers) or int(command[1]) <= 0:
                print("Invalid count")

            else:
                first_count = []
                for c in range(len(numbers)):
                    if int(numbers[c]) % 2 != 0:
                        first_count.append(numbers[c])
                        if len(first_count) == int(command[1]):
                            break
                        else:
                            continue
                print(list(map(int, first_count)))

    if "last" in command:
        if command[2] == "even":
            if int(command[1]) > len(numbers) or int(command[1]) <= 0:
                print("Invalid count")

            else:
                even_count = []
                for c in range(len(numbers)):
                    if int(numbers[c]) % 2 == 0:
                        even_count.append(numbers[c])

                print(list(map(int, even_count[-int(command[1]):])))
        if command[2] == "odd":
            if int(command[1]) > len(numbers) or int(command[1]) <= 0:
                print("Invalid count")

            else:
                odd_count = []
                for c in range(len(numbers)):
                    if int(numbers[c]) % 2 != 0:
                        odd_count.append(numbers[c])

                print(list(map(int, odd_count[-int(command[1]):])))
    command = input().split(" ")

print(list(map(int, numbers)))
