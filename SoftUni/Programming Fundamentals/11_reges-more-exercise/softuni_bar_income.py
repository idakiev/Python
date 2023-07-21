import re

pattern = r"\%([A-Z]{1}[a-z][^A-Z]+)\%[^\|\.\%\$]*\<(\w+)\>[^\|\.\%\$]*\|([\d]+)\|[^\|\.\%\$0-9]*([\d]+[\.\d]*)\$"

command = input()

total_income = 0

while command != "end of shift":

    result_regex = re.search(pattern, command)
    if result_regex:
        current_name = result_regex.group(1)
        current_item = result_regex.group(2)
        total_amount = int(result_regex.group(3)) * float(result_regex.group(4))
        total_income += total_amount
        print(f"{current_name}: {current_item} - {total_amount:.2f}")

    command = input()
print(f"Total income: {total_income:.2f}")
