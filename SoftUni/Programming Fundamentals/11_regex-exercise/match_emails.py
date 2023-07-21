import re

emails_string = input()

search_pattern = r"\s([a-z0-9]+?[a-z0-9\.\-\_]+?@[a-z]+[\.\-][a-z\-\.]+[a-z]?\b)"

result = re.findall(search_pattern, emails_string)

print('\n'.join(result))
