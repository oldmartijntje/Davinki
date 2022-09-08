import random
colors = ['Schoppen', 'Ruiten', 'Harten', 'Klaveren']
types = ['Aas', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer']
specials = ['Joker', 'Joker']
deck = list()
shuffledDeck = list()
for x in range(0, len(colors)):
    for y in range(0, len(types)): deck.append(colors[x] + " " + types[y])
for z in range(0, len(specials)):
    deck.append(specials[z])
for i in range(0, len(deck)):
    random_number = random.randint(0, len(deck)-1)
    shuffledDeck.append(deck[random_number])
    deck.pop(random_number)
for e in range(0, 7):
    print(shuffledDeck[0])
    shuffledDeck.pop(0)
print("deck (47 kaarten): ", shuffledDeck)
