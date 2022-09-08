from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
def move(num,direction,amount):
    for u in range(1,amount+1):
        robotArm.grab()
        e = robotArm.scan()
        if direction == "Left":
            if e != "":
                for ie in range(1,num+1):
                    robotArm.moveLeft()
                robotArm.drop()
                for i in range(1,num +1):
                    robotArm.moveRight()
        elif direction == "Right":
            if e != "":
                for ie in range(1,num+1):
                    robotArm.moveRight()
                robotArm.drop()
                for i in range(1,num +1):
                    robotArm.moveLeft()
        
    
        
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5
for i in range(1,8):
    robotArm.moveRight()
for i in range(1,9):
    move(1,"Right",1)
    robotArm.moveLeft()
    



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()