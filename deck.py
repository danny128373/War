import random
import settings
from card import Card


class Deck(Card):
    def __init__(self):
        self.all_cards = []

        for suit in settings.suits:
            for rank in settings.ranks:
                # Create card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
