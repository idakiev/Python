initial_deck = input()

faro_shuffle_count = int(input())

list_deck = initial_deck.split(" ")

left_deck = []
right_deck = []
shuffled_deck = []

mid_deck_index = len(list_deck) // 2

for shuffle in range(faro_shuffle_count):
    shuffled_deck = []
    for i in range(1):
        for k in range(0, mid_deck_index):
            left_deck.append(list_deck[k])
        for g in range(mid_deck_index, len(list_deck)):
            right_deck.append(list_deck[g])

    while len(left_deck) > 0:
        for v in left_deck:
            shuffled_deck.append(v)
            left_deck.remove(v)
            break
        for c in right_deck:
            shuffled_deck.append(c)
            right_deck.remove(c)
            break
    list_deck = shuffled_deck

print(shuffled_deck)
