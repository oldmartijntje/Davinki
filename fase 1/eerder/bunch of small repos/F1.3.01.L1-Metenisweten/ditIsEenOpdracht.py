getalA = int(input("geef maar een sappig getalletje "))
getalB = int(input("geef nog maar een sappig getalletje "))
gelijk = False
if getalA > getalB:
    max = getalA
    min = getalB
    print(f"a is het grootste getal: {max}")
elif getalA < getalB:
    max = getalB
    min = getalA
    print(f"b is het grootste getal: {max}")
else:
    print("‘a en b zijn even groot’")
    gelijk = True
if gelijk == False:
    print(f"‘Het minimum is: ’ gevolgd door de waarde van {min}")
    print(f"‘Het maximum is: ’ gevolgd door de waarde van {max}")
