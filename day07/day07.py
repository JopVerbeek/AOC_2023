from collections import Counter

with open('input7.txt') as f:
    lines = f.read().splitlines() 

def transform_hand(hand, q):
    cards = []
    lookup = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11 if q else 1,
        "T": 10
    }
    for item in hand:
        if item.isdigit():
            cards.append(int(item))
        else:
            cards.append(lookup[item])

    return cards

def hand_ranking(hand, q):
    hand = transform_hand(hand, q)    
    card_counts = Counter(hand)  
    card_counts_without_1 = Counter(hand)
    del card_counts_without_1[1]
    if not q:
        if 1 in card_counts.keys() and card_counts[1] != 5:            
            max_nums_cards = max(card_counts_without_1, key=card_counts.get)
            card_counts[max_nums_cards] += card_counts[1]
            del card_counts[1]           

    if sorted(card_counts.values()) == [5]:
        return (7, hand)
    elif sorted(card_counts.values()) == [1, 4]:
        return (6, hand)
    elif sorted(card_counts.values()) == [2, 3]:
        return (5, hand)
    elif sorted(card_counts.values()) == [1, 1, 3]:
        return (4, hand)
    elif sorted(card_counts.values()) == [1, 2, 2]:
        return (3, hand)
    elif sorted(card_counts.values()) == [1, 1, 1, 2]:
        return (2, hand)
    elif sorted(card_counts.values()) == [1, 1, 1, 1, 1]:
        return (1, hand)

for q in [True, False]:    
    hands_list = []
    for (hand, bet) in [line.split(' ') for line in lines]:
        rank = hand_ranking(hand, q)    
        hands_list.append((rank, int(bet)))        

    total = 0
    for i, (hand, bet) in enumerate(sorted(hands_list, key=lambda x:x[0]), start=1):        
        total += bet * i

    print(total)