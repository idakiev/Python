year = int(input())

current_number = -1

current_year = ""
list_current_year = []
is_happy_year = False

while not is_happy_year:
    year += 1
    for i in range(len(str(year))):
        current_digit = str(year)[i]
        if current_digit in list_current_year:
            current_year = ""
            current_number = -1
            list_current_year = []
            break
        else:
            current_number = current_digit
            current_year += str(current_number)
            list_current_year.append(current_number)
            continue
    if len(current_year) == len(str(year)):
        is_happy_year = True
        print(current_year)
        break
