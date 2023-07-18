import re

data = input()

search_pattern = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"

result = re.findall(search_pattern, data)

print(' '.join(result))
