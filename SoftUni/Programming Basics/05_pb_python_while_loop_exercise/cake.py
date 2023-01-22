cake_width = int(input())
cake_length = int(input())

total_pieces = cake_width * cake_length
total_pieces_eaten = 0

while True:
    pieces_eaten = input()
    if pieces_eaten != "STOP":
        total_pieces_eaten += int(pieces_eaten)
        if total_pieces < total_pieces_eaten:
            diff_pieces = abs(total_pieces - total_pieces_eaten)
            print(f"No more cake left! You need {diff_pieces} pieces more.")
            break

    elif pieces_eaten == "STOP":
        if total_pieces > total_pieces_eaten:
            diff_pieces = total_pieces - total_pieces_eaten
            print(f"{diff_pieces} pieces are left.")
            break
        else:
            diff_pieces = abs(total_pieces - total_pieces_eaten)
            print(f"No more cake left! You need {diff_pieces} pieces more.")
            break
