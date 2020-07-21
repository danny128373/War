from card import Card
from deck import Deck
from player import Player
import settings

player_one = Player("Jose")
player_two = Player("Daniel")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

round_num = 0
# while game_on
#     while at war
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Player Two Wins!")
        game_on = False
        break

    if len(player_one.all_cards) == 0:
        print("Player Two out of cards! Player One Wins!")
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
