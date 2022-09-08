from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5
round = 0
while True:
    robotArm.grab()
    e = robotArm.scan()
    print(e)
    if e == "white":
        
        robotArm.moveRight()
        robotArm.drop()
        
        robotArm.moveLeft()
    else:
        robotArm.moveRight()
    round += 1
    if round >= 4:
        break




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()