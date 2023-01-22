book_name = input()

book_counter = 0

while True:
    current_book = input()
    book_counter += 1
    if current_book != book_name and current_book != "No More Books":
        continue
    elif current_book == "No More Books":
        book_counter -= 1
        print(f"The book you search is not here!\n" f"You checked {book_counter} books.")
        break
    else:
        book_counter -= 1
        print(f"You checked {book_counter} books and found it.")
        break
