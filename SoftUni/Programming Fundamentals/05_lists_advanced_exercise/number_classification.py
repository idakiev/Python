
given_numbers = input().split(", ")

positive_numbers = ", ".join([x for x in given_numbers if int(x) >= 0])
negative_numbers = ", ".join([y for y in given_numbers if int(y) < 0])
even_numbers = ", ".join([z for z in given_numbers if int(z) % 2 == 0])
odd_numbers = ", ".join([i for i in given_numbers if int(i) % 2 != 0])

print(f"Positive: {positive_numbers}")
print(f"Negative: {negative_numbers}")
print(f"Even: {even_numbers}")
print(f"Odd: {odd_numbers}")
