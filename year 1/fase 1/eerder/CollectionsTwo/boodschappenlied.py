def toevoegenAanLijstje(boodschappen, newItem, amount):
    try: 
        boodschappen[newItem] += amount
    except:
        boodschappen[newItem] = amount
    print("so that makes " + str(boodschappen[newItem]) + " times " + newItem)
    return boodschappen
boodschappenLijstje = dict()
loop1 = 1
while loop1 == 1:
    answer1 = input("What do you want to add to the list?")
    if answer1 == "":
        break
    loop2 = 1
    while loop2 == 1:
        answer2 = input("How many times do you want " + answer1 + "?")
        try:
            answer2int = int(answer2)
            if answer2int > 0:
                loop2 = 0
            else:
                print("that is not a valid number of times you can buy something")
        except:
            print("that is not a valid number of times you can buy something")
    boodschappenLijstje = toevoegenAanLijstje(boodschappenLijstje, answer1, answer2int)
print(boodschappenLijstje)

