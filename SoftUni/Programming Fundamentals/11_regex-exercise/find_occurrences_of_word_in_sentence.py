import re

data = input()

search_pattern = fr'\b{input()}\b'

result = re.findall(search_pattern, data, re.I)

print(len(result))
