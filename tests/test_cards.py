from unittest.case import TestCase
from oop.cards import *

__author__ = 'Dmitry Mekhantev'


class TestCard(TestCase):
    def test_properties(self):
        deck = Deck((
            Card(2, Suit.Club),
            Card(10, Suit.Diamond),
            Card(12, Suit.Spade),
            Card(5, Suit.Heart)
        ))
        self.assertEqual(deck._cards[1].face, 10)
        self.assertEqual(deck._cards[2].suit, Suit.Spade)


class TestDeck(TestCase):
    def test_deal_card(self):
        deck = Deck([
            Card(2, Suit.Club),
            Card(10, Suit.Diamond),
            Card(12, Suit.Spade),
            Card(5, Suit.Heart)
        ])
        for _ in range(4):
            self.assertEqual(deck._cards[0], deck.deal_card())
        self.assertRaises(Exception, deck.deal_card)

    def test_remaining_cards(self):
        deck = Deck([
            Card(2, Suit.Club),
            Card(10, Suit.Diamond),
            Card(12, Suit.Spade),
            Card(5, Suit.Heart)
        ])
        for i in range(3, -1, -1):
            deck.deal_card()
            self.assertEqual(deck.remaining_cards(), i)


class TestHand(TestCase):
    def test_add_card(self):
        hand = Hand()
        card = Card(11, Suit.Club)
        hand.add_card(card)
        self.assertEqual(card, hand._cards[0])

    def test_remove_card(self):
        hand = Hand()
        cards = (
            Card(11, Suit.Club),
            Card(2, Suit.Diamond),
            Card(5, Suit.Spade)
        )
        for card in cards:
            hand.add_card(card)
        hand.remove_card(hand.cards[1])
        self.assertEqual(hand.cards, (cards[0], cards[2]))

    def test_remove_all_cards(self):
        hand = Hand()
        hand.add_card(Card(11, Suit.Club))
        hand.add_card(Card(2, Suit.Diamond))
        hand.add_card(Card(5, Suit.Spade))
        hand.remove_all_cards()
        self.assertEqual(len(hand._cards), 0)

