pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

hours_per_book = pages // pages_per_hour
days_required = hours_per_book // days_per_book

print(days_required)
