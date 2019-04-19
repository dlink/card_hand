#!/usr/bin/env python

from card_hand import best_hand

import unittest

class TestCardHard(unittest.TestCase):
    
    def test_royal_flush(self):
        hand = '0H JH QH KH AH'.split(' ')
        self.assertEqual(best_hand(hand),
                         'Royal Flush: AH KH QH JH 0H')
        
    def test_straight_flush(self):
        hand = '2C 3C 4C 5C 6C'.split(' ')
        self.assertEqual(best_hand(hand),
                         'Straight Flush: 6C 5C 4C 3C 2C')

    def test_four_of_a_kind(self):
        hand = '5S 5H 5D 5C AS'.split(' ')
        self.assertEqual(best_hand(hand),
                         'Four of a kind: 5S 5H 5D 5C AS')

    def test_full_house(self):
        hand = '8C 2S 2H 2D 8S'.split(' ')
        self.assertEqual(best_hand(hand),
                         'Full House: 2S 2H 2D 8C 8S')

    def test_flush(self):
        hand = 'KH 8H 2H 5H 3H'.split(' ')
        self.assertEqual(best_hand(hand),
                         'Flush: KH 8H 5H 3H 2H')

    def test_straight(self):
        hand = '6H 7C 0S 9H 8H'.split(' ')
        self.assertEqual(best_hand(hand),
                         'Straight: 0S 9H 8H 7C 6H')

    def test_three_of_a_kind(self):
        hand = 'QC 7C 0S QS QH'.split(' ')
        self.assertEqual(best_hand(hand),
                         'Three of a kind: QC QS QH 0S 7C')

    def test_two_pair(self):
        hand = 'AC 5C 5S 3S AH'.split(' ')
        self.assertEqual(best_hand(hand),
                         'Two Pair: AC AH 5C 5S 3S')

    def test_pair(self):
        hand = '5C 6C JS 0S JH'.split(' ')
        self.assertEqual(best_hand(hand),
                         'Pair: JS JH 0S 6C 5C')

    def test_high_card(self):
        hand = 'JC 6C 0S 2S 5H'.split(' ')
        self.assertEqual(best_hand(hand),
                         'High card: JC 0S 6C 5H 2S')


if __name__ == '__main__':
    unittest.main()
