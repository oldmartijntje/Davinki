

kaas = input('nummeroooo:\n>>>')
try:
    henk = int(kaas)
except Exception as e:
    print(e)
else:
    try:
        yeet = 100 / henk
    except Exception as ea:
        print(ea)
        raise NameError('Security breach suspected!')
    else:
        print(yeet)
finally:
    exit()