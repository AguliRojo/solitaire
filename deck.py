# Solitaire Klondike version
# rules: there are:
# 7 piles of cards we can stack cards from highest (K) to lowest (A).
# On empty fields we can put only (K),
# Each field has one uncovered card and (starting from 0) n+1 covered card
# 4 piles of cards we can stack cards from lowest (A) to highest (K). Its a win condition.
# 1 extra pile with random cards (1-3 are shown)

# deck declaration
deck = {"hearts": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
        "diamonds" : ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
        "spades": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
        "clubs": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]}


# used card pile during game declaration
used_cards = {"hearts": [],
            "diamonds": [],
            "spades": [],
            "clubs": []}

aces_pile = {1: [], 2: [], 3: [], 4: []}
game_pile = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
random_pile = {1: []}

deck_game = deck.copy()
used_cards_game = used_cards.copy()
aces_pile_game = aces_pile.copy()
game_pile_game = game_pile.copy()
random_pile_game = random_pile.copy()


# tests
print(deck_game["hearts"][3])
print(used_cards_game)



def asssign_game_pile(deck_game, used_cards_game, game_pile):
    try:
        used_cards_game["hearts"].append(deck_game["hearts"][2])
        used_cards_game["hearts"].append(game_pile["hearts"][2])
        del deck_game["hearts"][2]
    except:
        pass
    pass


# Using cards
def play_card(deck_game, used_cards_game):
    pass


try:
    used_cards_game["hearts"].append(deck_game["hearts"][2])
    del deck_game["hearts"][2]
except: pass

#verification
print(deck_game)
# print(used_cards)