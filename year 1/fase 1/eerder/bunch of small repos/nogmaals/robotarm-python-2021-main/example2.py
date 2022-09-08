from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5
round = 0
while True:
    robotArm.grab()
    e = robotArm.scan()
    if e == "blue":
        for ie in range(1,10-round):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(1,9 - round):
            robotArm.moveLeft()
    else:
        robotArm.moveRight()
    round += 1
    if round >= 9:
        break
        



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()