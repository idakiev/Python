import re

data_count = int(input())

search_pattern = r"@[\#]+([A-Z]{1}[a-zA-Z0-9]{4,}[A-Z]{1})@[\#]+"

for i in range(data_count):
    current_data = input()
    valid_data = re.search(search_pattern, current_data)
    if valid_data:
        barcode_to_check = valid_data.group(1)
        current_group = ""
        for k in barcode_to_check:
            if k.isdigit():
                current_group += k
        if current_group:
            print(f"Product group: {current_group}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
