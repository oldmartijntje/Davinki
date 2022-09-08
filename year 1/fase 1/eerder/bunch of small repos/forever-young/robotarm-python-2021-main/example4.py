from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
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

move(2,"Right",3)
robotArm.moveRight()
robotArm.moveRight()
move(1,"Left",3)
robotArm.moveLeft()
robotArm.moveLeft()
        



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()