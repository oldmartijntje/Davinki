from RobotArm import RobotArm

robotArm = RobotArm('assessment1')
robotArm.speed=1

# Jouw python instructies zet je vanaf hier:
def switch():
    for x in range(3):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveLeft()
def moveLeft(amount):
    for z in range(amount): robotArm.moveLeft()
def moveRight(amount):
    for z in range(amount): robotArm.moveRight()
for x in range(4):
    robotArm.moveRight()
switch()
for x in range(3):
    robotArm.grab()
    moveLeft(3)
    robotArm.drop()
    moveRight(3)
moveRight(2)
switch()
for x in range(3):
    robotArm.grab()
    moveRight(5)
    robotArm.drop()
    moveLeft(5)



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()