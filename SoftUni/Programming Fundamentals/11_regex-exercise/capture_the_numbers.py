import re

data_strings = input()

while data_strings != "":

    search_pattern = r"[0-9]?\d+"

    result = re.finditer(search_pattern, data_strings)
    for match in result:
        print(match.group(), end=" ")
    # print(result)
    data_strings = input()
