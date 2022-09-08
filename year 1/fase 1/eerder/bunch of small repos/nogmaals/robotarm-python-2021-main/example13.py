from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)   
# Jouw python instructies zet je vanaf hier:
loop = 1
rounds = 0
while loop == 1:
    robotArm.grab()
    scan = robotArm.scan()
    if scan != "":
        rounds += 1
        for x in range(0,rounds):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,rounds):
            robotArm.moveLeft()
    else:
        loop = 0

    




# Na jouw code wachten tot het sluiten van de window:
 
 
robotArm.wait()