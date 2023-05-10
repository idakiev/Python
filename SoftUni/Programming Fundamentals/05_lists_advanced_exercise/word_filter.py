
some_text = input().split(" ")

even_length_text = [x for x in some_text if len(x) % 2 == 0]

for i in even_length_text:
    print(i)
