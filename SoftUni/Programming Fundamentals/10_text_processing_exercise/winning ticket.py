

def check_ticket(ticket: str):
    left_part = ticket[0:10]
    right_part = ticket[10:]
    winning_symbols = ['@', '#', '$', '^']
    previous_symbol = ""
    winning_sequence = 0
    left_side_score = 0
    left_side_symbol = ""
    right_side_score = 0

    for symbol in left_part:
        if symbol in winning_symbols:
            if symbol == previous_symbol:
                winning_sequence += 1
            else:
                if winning_sequence < 6:
                    previous_symbol = symbol
                    winning_sequence = 1
                else:
                    break
        else:
            if winning_sequence < 6:
                previous_symbol = ""
                winning_sequence = 0
            else:
                break
    if winning_sequence >= 6:
        left_side_score = winning_sequence
        left_side_symbol = previous_symbol
        previous_symbol = ""
        winning_sequence = 0
        for symbol in right_part:
            if symbol == left_side_symbol:
                if symbol == previous_symbol:
                    winning_sequence += 1
                else:
                    if winning_sequence < 6:
                        previous_symbol = symbol
                        winning_sequence = 1
                    else:
                        break
            else:
                if winning_sequence < 6:
                    previous_symbol = ""
                    winning_sequence = 0
                else:
                    break
        if winning_sequence >= 6:
            right_side_score = winning_sequence
    if left_side_score >= 6 and right_side_score >= 6:
        if left_side_score == 10 and right_side_score == 10:
            return f"{min(left_side_score, right_side_score)}{left_side_symbol} Jackpot!"
        else:
            return f"{min(left_side_score, right_side_score)}{left_side_symbol}"
    else:
        return "no match"


initial_input = input().split(",")

tickets_to_check = [x.strip() for x in initial_input]


for i in tickets_to_check:
    current_ticket = i
    if len(current_ticket) != 20:
        print(f"invalid ticket")
    else:
        # check_ticket(i)
        print(f'ticket "{current_ticket}" - {check_ticket(i)}')
