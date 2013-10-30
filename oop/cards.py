from abc import ABCMeta
from collections.abc import Iterable
from enum import Enum


class Suit(Enum):
    Club = 0
    Diamond = 1
    Heart = 2
    Spade = 3


class Card:
    @property
    def face(self):
        return self._face

    @property
    def suit(self):
        return self._suit

    def __init__(self, face: int, suit: int):
        self._face = face
        self._suit = suit

    def __eq__(self, other):
        return (self.face == other.face
                and self.suit == other.suit)


class CardsHolder(metaclass=ABCMeta):
    def __init__(self):
        self._cards = []


class NoCardsError(Exception):
    pass


class Deck(CardsHolder):
    def __init__(self, cards: Iterable):
        super().__init__()
        self._cards.extend(cards)

    def deal_card(self):
        if self.remaining_cards() == 0:
            raise NoCardsError('No cards left')
        return self._cards.pop(0)

    def remaining_cards(self):
        return len(self._cards)


class Hand(CardsHolder):
    @property
    def cards(self):
        return tuple(self._cards)

    def add_card(self, card: Card):
        self._cards.append(card)

    def remove_card(self, card: Card):
        self._cards.remove(card)

    def remove_all_cards(self):
        cards = tuple(self._cards)
        self._cards.clear()
        return cards







