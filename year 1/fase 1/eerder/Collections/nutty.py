import random
def dictShuffle(zakOmTeSorteren):
    bigToSmall = list()
    sorter = ["oranje", "blauw", "groen", "bruin"]
    for i in range(0,4):
        biggest = 0
        for x in range(0, len(sorter)):
            if x == 0:
                biggest = x
            elif zakOmTeSorteren[sorter[x]] > zakOmTeSorteren[sorter[biggest]]:
                biggest = x
        bigToSmall.append(sorter[biggest])
        sorter.remove(sorter[biggest])
    print(f"{bigToSmall[0]}:{zakOmTeSorteren[bigToSmall[0]]}, {bigToSmall[1]}:{zakOmTeSorteren[bigToSmall[1]]}, {bigToSmall[2]}:{zakOmTeSorteren[bigToSmall[2]]}, {bigToSmall[3]}:{zakOmTeSorteren[bigToSmall[3]]}")
def zakSorteren(zakOmTeSorteren):
    if type(zakOmTeSorteren) == dict:
        print("dict")
        dictShuffle(zakOmTeSorteren)
    elif type(zakOmTeSorteren) == list:
        print("list")
        amount = {

            'oranje': 0,
            'blauw' : 0,
            'groen' : 0,
            'bruin' : 0
        }
        for x in range(0, len(zakOmTeSorteren)):
            amount[zakOmTeSorteren[0]]+=1    
            zakOmTeSorteren.remove(zakOmTeSorteren[0])
        dictShuffle(amount)
def zakjeMEnMs(kleuren):
    zakMEnMs = list()
    mnmDictionaryBag = {

            'oranje': 0,
            'blauw' : 0,
            'groen' : 0,
            'bruin' : 0
        }
    while True:
        try:
            aantalKeer = int(input("hoeveel M&M's"))
            break
        except:
            print("what about a number?")
    for x in range(0, aantalKeer):
        kleurenNummer = random.randint(0, 3)
        zakMEnMs.append(kleuren[kleurenNummer])
        mnmDictionaryBag[kleuren[kleurenNummer]]+=1
    zakSorteren(mnmDictionaryBag) 
    zakSorteren(zakMEnMs)                                       
    return mnmDictionaryBag

kleurtjes = ["oranje", "blauw", "groen", "bruin"]
MEnMs = zakjeMEnMs(kleurtjes)
MEnMs = zakjeMEnMs(kleurtjes)