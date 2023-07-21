import re

data = input()

search_pattern = r"(?<=\W_)[a-zA-Z0-9]+(?!\w)"

result = re.findall(search_pattern, data)

print(','.join(result))
