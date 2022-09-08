import random, os, sys, string
alphabet_lower_string = string.ascii_lowercase
alphabet_upper_string = string.ascii_uppercase
digits = string.digits
alphabet_lower_list = list(alphabet_lower_string)
alphabet_upper_list = list(alphabet_upper_string)
number_list = list(digits)
characters_list = ['@', '#', '$', '%', '&', '_', '?']
def shuffler(currentPassword: list):
    shuffledPassword = list()
    for i in range(0, len(currentPassword)):
        random_number = random.randint(0, len(currentPassword)-1)
        shuffledPassword.append(currentPassword[random_number])
        currentPassword.pop(random_number)
    return shuffledPassword

def checker(currentPassword: list):
    while currentPassword[len(currentPassword)-1] in characters_list or currentPassword[2] in number_list or currentPassword[1] in number_list or currentPassword[0] in number_list or currentPassword[0] in characters_list:
        while currentPassword[len(currentPassword)-1] in characters_list:
            currentPassword.append(currentPassword[3])
            currentPassword.pop(3)
        while currentPassword[2] in number_list:
            currentPassword.append(currentPassword[2])
            currentPassword.pop(2)
        while currentPassword[1] in number_list:
            currentPassword.append(currentPassword[1])
            currentPassword.pop(1)
        while currentPassword[0] in number_list or currentPassword[0] in characters_list:
            currentPassword.append(currentPassword[0])
            currentPassword.pop(0)
    return currentPassword

def listToString(passwordList):
    passwordString = "".join(str(x) for x in passwordList)
    return passwordString

def setup():
    wachtwoordList = list()
    random_hoofdletter = random.randint(2, 6)
    random_cijfers = random.randint(4, 7)
    for x in range(0, 3):wachtwoordList.append(characters_list[random.randint(0, len(characters_list) - 1)])
    for x in range(0, random_hoofdletter):wachtwoordList.append(alphabet_upper_string[random.randint(0, len(alphabet_upper_string) - 1)])
    for x in range(0, random_cijfers):wachtwoordList.append(number_list[random.randint(0, len(number_list) - 1)])
    for x in range(0, 8 + (24 - len(wachtwoordList))):wachtwoordList.append(alphabet_lower_list[random.randint(0, len(alphabet_lower_list) - 1)])
    for x in range(0, random.randint(1, 69)):
        wachtwoordList = shuffler(wachtwoordList)
    wachtwoordList = checker(wachtwoordList)
    password = listToString(wachtwoordList)
    return password

def checkForNumber(string: str = "input a number", mode:str ="",number:int = 0):
    #made this so i can copy this to any project
    loop1 = 1
    while loop1 == 1:
        amountStr = input(string)
        try:
            amount = int(amountStr)
            if mode == ">":
                if amount > number:
                    loop1 = 0
                else:
                    print("sorry, the number has to be bigger than", number)
            elif mode == "<":
                if amount < number:
                    loop1 = 0
                else:
                    print("sorry, the number has to be smaller than", number)
            elif mode == "<=":
                if amount <= number:
                    loop1 = 0
                else:
                    print("sorry, the number has to be smaller than", number + 1)
            elif mode == ">=":
                if amount >= number:
                    loop1 = 0
                else:
                    print("sorry, the number has to be bigger than", number - 1)
            elif mode == "==" or mode == "=":
                if amount == number:
                    loop1 = 0
                else:
                    print("sorry, the number has to be", number)
            else:
                loop1 = 0
        except:
            print("that is not a number")
    return amount
    
amount = checkForNumber("how many passwords?",">",0)
for x in range(amount):
    print(setup())

