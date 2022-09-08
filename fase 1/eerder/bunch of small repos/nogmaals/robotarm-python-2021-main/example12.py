from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')     
# Jouw python instructies zet je vanaf hier:
for x in range(0,8):
    robotArm.moveRight()
for x in range(1,9):
    robotArm.grab()
    scan = robotArm.scan()
    if scan == "red":
        for c in range(0,x):
            robotArm.moveRight()
        robotArm.drop()  
        for c in range(0,x):
            robotArm.moveLeft()  
    else:
        robotArm.drop()
    robotArm.moveLeft()

    




# Na jouw code wachten tot het sluiten van de window:
 
 
robotArm.wait()