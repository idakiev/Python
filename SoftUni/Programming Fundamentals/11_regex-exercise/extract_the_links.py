import re

urls_to_check = input()

search_pattern = r"(www.[a-zA-Z0-9\-]+\.[a-z\.]+)"

while urls_to_check:
    result = re.search(search_pattern, urls_to_check)
    if result:
        print(result.group(0))

    urls_to_check = input()
