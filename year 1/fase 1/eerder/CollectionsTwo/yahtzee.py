import random, sys, time, time, os
#0.letter for letter, 1.text to speech(no funtionality), 2.textspeed, 3.text to speech voice (no functionality) , 4.endgame( port compatebility (does nothing), 5.deley between 1 by 1 letter
#6.amount of dice, 7.amount of sides a dice has
options = [1, 0, 1.4, 1, 0, 0.1, 5, 6, 3]
gameOptions = ['aces', 'twos', 'threes', 'fours', 'fives', 'sixes', 'three of a kind', 'four of a kind', 'full house', 'small straight', 'large straight', 'yahtzee', 'chance']


#clear the console
def clear_console():
    try:
        os.system('cls')
    except:
        try:
            os.system('clear')
        except:
            e = 0

#a function from my game which makes letters come in 1 by 1
def printing(text): 
    if options[0] == 1: #if 1 by 1 turned on 
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(options[5])
        print()
        if 0 != 0:  #turned off
            time.sleep(0 / options[2])
    else:
        print(text)

#check if it is an intager
def checkForIntager(choice, mode):
    intager = False
    try:    #see if it is an intager by seeing if it gets an exception whilst making string an int
        choice[mode] = int(choice[mode])
        intager = True
    except:
        print("sorry, but the thing behind the . should be a intager that corresponds to one of the dice")
    return intager

#dobble all the dice that have 0
def dobble(dice):
    for x in range(0, len(dice)):   #for every dce that is -1, replace it by random number
        if dice[x] == -1:
            dice[x] = random.randint(1,options[7])
    return dice

#gets the dice you are going to keep and reroll in lists
def checkTheRerolls(dice, game, rerolls):
    kept = list()
    rerolling = list()
    keeping = list()
    for x in range(options[6]):
        if rerolls[x] == "reroll":  #adds dice number to whatever list it belongs
            rerolling.append(dice[x])
        else:
            keeping.append(dice[x])
    return rerolling, keeping, kept


#the part that prints everything, to be able to be used eveerywhere
def easyPrint(dice, game, rerolls, timesRolledTheDice, scoreNow):
    clear_console()
    print(f"current score: {scoreNow}")
    print("your options are:")
    openOptionsString = ""#show all the items you haven't crossed off before
    for x in range(len(gameOptions)):
        if game[gameOptions[x]] == -2:
            openOptionsString += "| "+gameOptions[x]+" | "
    print(openOptionsString)
    print("your dice: " + str(dice)+f"\nyou have rolled the dice {timesRolledTheDice}/3 times\n")
    print("to keep, type \"keep.\" and then the number of the dice\nto roll again, type \"roll.\" and then the number of the dice")
    print("to continue with the changes, say \"continue\"\nto use the dice early, say \"fill\"")
    rerolling, keeping, keptAnotherRoll = checkTheRerolls(dice, game, rerolls)#checking what dice is in what list
    print(f"current settings: you are going to keep {keeping}, and reroll {rerolling}")
    return rerolling, keeping, keptAnotherRoll

#choose which dices you keep and which ones u don't
def dicePicker(dice, game, rerolls, turn, score):
    notDone = True
    dice = dobble(dice)# dobble (randomize the dice with the value -1)
    rerolling, keeping, keptAnotherRoll = easyPrint(dice, game, rerolls, turn, score)# show the text that tells you what options you have, and what your dice are
    choice = input().split('.')#look at what your input is
    if choice[0].lower() != "keep" and "keep" in choice[0].lower():    #2 type error
        print("sorry, didn't pick it up, make sure u say \"keep\", then a '.' and then the number")
    elif choice[0].lower() != "roll" and "roll" in choice[0].lower():  #2 type error
        print("sorry, didn't pick it up, make sure u say \"roll\", then a '.' and then the number")
    elif choice[0].lower() == "keep" and choice[1] == "order":    #keep the ___ dice from list order
        results = checkForIntager(choice, 2)
        if results == True and int(choice[2]) <= len(rerolling) and int(choice[2]) > 0:#check if it is a valid number
            found = False
            for x in range(len(rerolls)):
                if found == False:
                    if rerolls[x] == "reroll" and dice[x] == rerolling[int(choice[2])-1]:
                        rerolls[x] = "keep"
                        found = True
    elif choice[0].lower() == "keep":   #keep a dice with the number as amount
        results = checkForIntager(choice, 1)
        for x in range(0, len(rerolls)):
            if results == True and dice[x] == int(choice[1]) and rerolls[x] == "reroll":
                rerolls[x] = "keep"
                break
    elif choice[0].lower() == "roll" and choice[1] == "order":  #roll the ___ dice from list order
        results = checkForIntager(choice, 2)
        if results == True and int(choice[2]) <= len(keeping) and int(choice[2]) > 0:#check if it is a valid number
            found = False
            for x in range(len(rerolls)):
                if found == False:
                    if rerolls[x] == "keep" and dice[x] == keeping[int(choice[2])-1]:
                        rerolls[x] = "reroll"
                        found = True
    elif choice[0].lower() == "roll":   #roll dice with number as amount
        results = checkForIntager(choice, 1)
        for x in range(0, len(rerolls)):
            if results == True and dice[x] == int(choice[1]) and rerolls[x] == "keep":
                print(x)
                rerolls[x] = "reroll"
                break
    elif choice[0].lower() == "continue" or choice[0].lower() == "play":   #do the things it needs when you chose to roll the dice again
        for i in range(0, len(rerolls)):
            if rerolls[i] == "reroll" and turn != options[8]:
                dice[i] = -1
        notDone = False
    elif choice[0].lower() == "fill":   #do the things it needs when you chose to roll the dice again
        for i in range(0, len(rerolls)):
            if rerolls[i] != "reroll":
                rerolls[i] = "reroll"
        turn = 2
        notDone = False
    return notDone, dice, turn, rerolls                

#function for ez calculation
def numberCalculation(number, dice):
    score = 0
    for x in range(options[6]):
        if dice[x] == number:
            score += number
    return score

#checks the score you will get
def calculateScore(dice, game, rerolls, choice):
    score = 0
    if game["yahtzee"] != -2 and game["yahtzee"] != 0:
        for x in range(1, options[6]+ 1):
            test = dice.count(x)
            if test == options[6]:
                score += 100
    if choice == "aces":
        score += numberCalculation(1, dice)
    elif choice == "twos":
        score += numberCalculation(2, dice)
    elif choice == "threes":
        score += numberCalculation(3, dice)
    elif choice == "fours":
        score += numberCalculation(4, dice)
    elif choice == "fives":
        score += numberCalculation(5, dice)
    elif choice == "sixes":
        score += numberCalculation(6, dice)
    elif choice == "three of a kind":
        succes = False
        for x in range(1, options[6]+ 1):
            test = dice.count(x)
            if test >= 3:
                succes = True
        if succes == True:
            for x in range(options[6]):
                score += dice[x]
    elif choice == "four of a kind":
        succes = False
        for x in range(1, options[6]+ 1):
            test = dice.count(x)
            if test >= 4:
                succes = True
        if succes == True:
            for x in range(options[6]):
                score += dice[x]
    elif choice == "full house":
        succes = [False,False]
        for x in range(1, options[6]+ 1):
            test = dice.count(x)
            if test == 3:
                succes[0] = True
            elif test == 2:
                succes[1] = True
        if succes[0] == True and succes[1] == True:
            score += 25
    elif choice == "small straight":
        succes = False
        for x in range(options[6]):
            if dice[x]+1 in dice and dice[x]+2 in dice:
                succes = True
        if succes == True:
            score += 30
    elif choice == "large straight":
        succes = False
        for x in range(options[6]):
            if dice[x]+1 in dice and dice[x]+2 in dice and dice[x]+3 in dice:
                succes = True
        if succes == True:
            score += 40
    elif choice == "yahtzee":
        for x in range(1, options[6]+ 1):
            test = dice.count(x)
            if test == options[6]:
                score += 50
    elif choice == "chance":
        for x in range(options[6]):
            score += dice[x]
    return score



#the turns system
def turn(dice, game, rerolls):
    currentScore = 0
    activeGame = True
    while activeGame == True:
        turnOfPlayer = True
        turn = 0
        while turnOfPlayer == True:
            turn += 1
            print(turn)
            deciding = True
            while deciding == True:
                deciding, dice, turn, rerolls  = dicePicker(dice, game, rerolls, turn, currentScore)
            if turn == options[8] -1:
                turnOfPlayer = False 
        clear_console()
        dice = dobble(dice)
        print(f"you have rolled the dice {options[8]} times, now you have to choose where you want to use the dice")
        print("your dice: " + str(dice))
        for i in range(options[6]):
            if rerolls[i] != "reroll":
                rerolls[i] = "reroll"
        openOptionsString = ""#show all the items you haven't crossed off before
        for x in range(len(gameOptions)):
            if game[gameOptions[x]] == -2:
                openOptionsString += "| "+gameOptions[x]+" | "
        fillSomethinInLoop = True
        while fillSomethinInLoop == True:
            print(openOptionsString)
            print("\ntype the name of the thing you want to fill in")
            fillIn = input()
            testException = True
            try:
                test = game[fillIn.lower()]
                testException = True
            except:
                print("that is not an option")
                testException = False
            if testException == True:
                if game[fillIn.lower()] == -2:
                    score = calculateScore(dice, game, rerolls, fillIn.lower())
                    #print(f"you obtained a score of {score}")
                    currentScore += score
                    game[fillIn.lower()] = score
                    fillSomethinInLoop = False
                else:
                    print("That space is already filled in")
        for x in range(options[6]):
            dice[x] = -1
        if -2 in game.values():
            activeGame = True
        else:
            activeGame = False
    
    return game
            
#calculates total score
def calculateTotalScore(game):
    score1 = game["aces"] + game["twos"] + game["threes"] + game["fours"] + game["fives"] + game["sixes"] 
    score2 = game["three of a kind"] + game["four of a kind"] + game["full house"] + game["small straight"] + game["large straight"] + game["yahtzee"] + game["chance"]
    if score1 > 63: score1 += 35
    score = score1 + score2
    return score

dice = list()
rerolls = list()
for x in range(options[6]):
    dice.append(-1)
    rerolls.append("reroll")
game = {
    "aces" : -2,
    "twos" : -2,
    "threes" : -2,
    "fours" : -2,
    "fives" : -2,
    "sixes" : -2,
    "three of a kind" : -2,
    "four of a kind" : -2,
    "full house" : -2,
    "small straight" : -2,
    "large straight" : -2,
    "yahtzee" : -2,
    "chance" : -2
}
activeTurn = 1
while activeTurn == 1:
    game = turn(dice, game, rerolls)
    score = calculateTotalScore(game)
    print(f"your final score is {score}!")
    input()