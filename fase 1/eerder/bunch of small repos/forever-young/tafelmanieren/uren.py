for i in range(1,13):
    if i != 12:
        print(str(i) + ":00 AM")
    else:
        print(str(i) + ":00 PM")
for i in range(1,13):
    if i != 12:
        print(str(i) + ":00 PM")
    else:
        print(str(i-12) + "0:00 AM")
input()