from RobotArm import RobotArm

robotArm = RobotArm('assessment2')
robotArm.speed=1

# Jouw python instructies zet je vanaf hier:
def moveArm(direction, amount):
    for x in range(amount):
        if direction == "right":robotArm.moveRight()
        elif direction == "left":robotArm.moveLeft()
def moveBlock(direction, amount):
    robotArm.grab()
    for x in range(amount):
        if direction == "right":robotArm.moveRight()
        elif direction == "left":robotArm.moveLeft()
    robotArm.drop()
    for x in range(amount):
        if direction == "right":robotArm.moveLeft()
        elif direction == "left":robotArm.moveRight()
# Onderstaande code pas je NIET aan

moveArm("right", 3);
moveBlock("left", 3);
moveBlock("right", 6);
moveBlock("right", 2);
moveBlock("right", 6);
moveBlock("left", 1);
moveBlock("left", 3);

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()