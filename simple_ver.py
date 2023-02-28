import random
# def card():
#   pass
# TODO: More card piles, proper card stacking

cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
deck_pile = cards
random.shuffle(deck_pile)
print(deck_pile)
operations = [1,2]
piles = [[]]
game = 1
# print(len(piles))
input("Start game")
for i in range(len(piles)):
  piles[0].append(deck_pile[0])
  deck_pile.pop(0)
while game:
    # Game setup
    bread = input(f'Deck file card:[\'{deck_pile[0]}\']\n '
                  f'Pile card:{piles[-1]}\n 1. Check next card\n'
                  f'2. Add to pile')
    if bread=="1":
      print("bread ok")
      deck_pile.append(deck_pile[0])
      deck_pile.pop(0)
      continue
    if bread=="2":
      print("To which pile? (1-7)")
      piles[0].append(deck_pile[0])
      deck_pile.pop(0)
      print(f'Cards left: {len(deck_pile)}')
      # if piles[[-1]]  # card stacking
    else:
      print(f'which moron picked {bread}')
    if piles[0] == "A" or len(deck_pile) == 0:
      print("You won")
      break
