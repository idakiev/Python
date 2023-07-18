import re

data = input()

search_pattern = r"\b([0-9]{2})([.|\-|\/])([A-Z]{1}[a-z]{2})\2([0-9]{4})\b"

result = re.findall(search_pattern, data)\

for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
