from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')     
# Jouw python instructies zet je vanaf hier:
for x in range(0,5):
    for y in range(0,7):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight()
    robotArm.moveRight()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()