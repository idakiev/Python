import re

data = input()

search_pattern = r"\+359 2 [0-9]{3} [0-9]{4}\b|\+359-2-[0-9]{3}-[0-9]{4}\b"

result = re.findall(search_pattern, data)

print(', '.join(result))
