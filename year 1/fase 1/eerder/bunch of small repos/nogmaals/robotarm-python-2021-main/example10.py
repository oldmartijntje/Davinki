  
from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')     
# Jouw python instructies zet je vanaf hier:
for x in range(0,5):
    robotArm.grab()
    for c in range(0,9-(2*x)):
        robotArm.moveRight()
    robotArm.drop()
    for c in range(0,9-(2*x)-1):
        robotArm.moveLeft()

    




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()