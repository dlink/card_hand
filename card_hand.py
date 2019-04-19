#!/usr/bin/env python

'''Evaluate a Poker Hand'''

import sys
from copy import copy

SUITS = 'HCDS'
ORDER  = '234567890JQKA'
ORDER2 = 'A234567890JQK'
RANK = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}
RANK2 = copy(RANK)
RANK2['A'] = 14

def best_hand(cards):
    '''Given a hand of 5 cards as an array
       Evaluate and
       Return a string that states 
           the best poker hand and the cards in proper order
    '''
    high_card_order = ' ' .join(sorted(cards,
                                       key=lambda x: RANK[x[0]],
                                       reverse=True))
    high_card_order2 = ' ' .join(sorted(cards,
                                       key=lambda x: RANK2[x[0]],
                                       reverse=True))
    card_order = None
    numbers = {}
    suits = {}
    for card in cards:
        ord = card[0]
        suit = card[1]

        if ord not in numbers:
            numbers[ord] = []
        numbers[ord].append(card)
        if suit not in suits:
            suits[suit] = []
        suits[suit].append(card)
        
    # Calc Flush
    flush = False
    if len(suits.keys()) == 1:
        flush = True
        
    # Calc Straight
    straight = False
    if len(numbers.keys()) == 5:
        n = sorted(numbers.keys(), key=lambda c: RANK2[c[0]])
        if len(range(RANK2[n[0]], RANK2[n[4]]+1)) == 5:
            card_order = high_card_order2
            straight = True
        n = sorted(numbers.keys(), key=lambda c: RANK[c[0]])
        if len(range(RANK[n[0]], RANK[n[4]]+1)) == 5:
            card_order = high_card_order
            straight = True
            
    # calc of a kind
    four_of_a_kind = full_house = three_of_a_kind = two_pair = pair = False
    four_set = []
    three_set = []
    two_set = []
    one_set = []
    for k,v in numbers.items():
        if len(v) == 4:
            four_set.append(v)
        elif len(v) == 3:
            three_set.append(v)
        elif len(v) == 2:
            two_set.append(v)
        elif len(v) == 1:
            one_set.append(v)
    if four_set:
        four_of_a_kind = True
        card_order = ' ' .join(four_set[0] + one_set[0])
    elif three_set:
        if two_set:
            full_house = True
            card_order = ' ' .join(three_set[0] + two_set[0])
        else:
            three_of_a_kind = True
            other = sorted(one_set, key=lambda ca: RANK2[ca[0][0]],
                           reverse=True)
            card_order = ' ' .join(three_set[0] + other[0] + other[1])
    elif two_set:
        if len(two_set) == 2:
            two_pair = True
            pairs = sorted(two_set, key=lambda ca: RANK2[ca[0][0]],
                           reverse=True)
            card_order = ' ' .join(pairs[0] + pairs[1] + one_set[0])
        else:
            pair = True
            other = sorted(one_set, key=lambda ca: RANK2[ca[0][0]],
                           reverse=True)
            card_order = ' ' .join(two_set[0] + other[0] + other[1] + other[2])
        
    # HERE WE GO

    if straight and flush and card_order[0] == 'A':
        return "Royal Flush: " + high_card_order2
    if straight and flush:
        return "Straight Flush: " + high_card_order2
    if four_of_a_kind:
        return 'Four of a kind: ' + card_order
    if full_house:
        return 'Full House: ' + card_order
    if flush:
        return 'Flush: ' + high_card_order2
    if straight:
        return 'Straight: ' + card_order
    if three_of_a_kind:
        return 'Three of a kind: ' + card_order
    if two_pair:
        return 'Two Pair: ' + card_order
    if pair:
        return 'Pair: ' + card_order
    return 'High card: ' + high_card_order2

def syntax():
    print "cards <c1> <c2> <c3> <c4> <c4>"
    exit(0)
    
# Main

# get cards from command line
if __name__ == '__main__':
    if len(sys.argv) != 6:
        syntax()

    cards = []
    for i in range(1, 6):
        cards.append(sys.argv[i].upper())

    # validate cards

    errors = []
    for i, card in enumerate(cards):
        card_str = 'Card %s (%s)' % (i+1, card)
        if len(card) != 2:
            errors.append('%s: Card can only have two charactors' % card_str)
        elif card[0] not in ORDER:
            errors.append('%s: First char must be one of %s' % (card_str,
                                                                ORDER))
        elif card[1] not in SUITS:
            errors.append('%s: Second char must be one of %s' % (card_str,
                                                                 SUITS))
    if errors:
        print 'Errors:'
        print '\n'.join(errors)
        sys.exit(1)

    print best_hand(cards)
