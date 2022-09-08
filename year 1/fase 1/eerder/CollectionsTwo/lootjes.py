import random

def lootjesPicken(namen, loten, number, resLootjes):
    while True:
        randomNummer = random.randint(0,len(resLootjes)- 1)
        if namen[number] != resLootjes[randomNummer]:
            break
    loten[number] = resLootjes[randomNummer]
    resLootjes.pop(randomNummer)
    return loten, resLootjes
    

namenLijstje = list() #maak de lijst
lootjes = list()
restrerendeLootjes = list()
namenVraagRondje = True #zorg voor de loop
print("geef drie+ namen, laat leeg als je niemand meer nodig hebt")
while namenVraagRondje == True:
    antwoord = input()
    if antwoord != "": #als het niet leeg is
        if antwoord not in namenLijstje:
            namenLijstje.append(antwoord)
    else:
        namenVraagRondje = False #stop de loop
if len(namenLijstje) > 2:
    for x in range(len(namenLijstje)):
        lootjes.append(namenLijstje[x])
        restrerendeLootjes.append(namenLijstje[x])
    testEnvirement = True
    for x in range(len(namenLijstje)):
        lootjes, restrerendeLootjes = lootjesPicken(namenLijstje, lootjes, x, restrerendeLootjes)
    for x in range(len(namenLijstje)):
        print(f"{namenLijstje[x]} heeft {lootjes[x]}'s lootje getrokken")