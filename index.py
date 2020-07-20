from card import Card
from deck import Deck
from player import Player
import settings

two_hearts = Card("Hearts", "Two")
three_clubs = Card("Clubs", "Three")
new_deck = Deck()

# print(settings.values[two_hearts.rank])
# print(settings.values[three_clubs.rank])
# print(new_deck.all_cards)
print(new_deck.all_cards[-1])
new_deck.shuffle()
my_card = new_deck.deal_one()
print(my_card)
print(len(new_deck.all_cards))
new_player = Player("Jose")
print(new_player)
new_player.add_cards(my_card)
new_player.add_cards(my_card)
new_player.add_cards(my_card)
print(new_player)

for card in new_player.all_cards:
    print(f"{new_player.name} has the card: {card}")
