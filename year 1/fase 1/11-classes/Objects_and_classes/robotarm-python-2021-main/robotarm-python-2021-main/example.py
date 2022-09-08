from RobotArm import SmartRobotArm

robotArm = SmartRobotArm()
robotArm.loadMyLevel([["green","white"],["green"],["white"],["green","white"],["red","white"],["white","white"],["blue"],["blue","blue","blue"],["blue", "green", "green"],["red"]])

# Jouw python instructies zet je vanaf hier:
robotArm.getNextColorRight('green')
robotArm.drop()
robotArm.moveStackTo(3)
robotArm.moveRightTimes(6)
robotArm.moveTo(3)
robotArm.moveStackTo(2)
robotArm.moveTo(2)
robotArm.moveStackTo(4)
robotArm.moveTo(4)
robotArm.moveStackTo(5)
robotArm.moveTo(5)
robotArm.moveStackTo(6)
robotArm.moveTo(6)
robotArm.moveStackTo(7)
print(robotArm.getStackSize(3))

robotArm.moveLeftTimes(3)

robotArm.moveLeft()

robotArm.moveTo(5)
robotArm.moveTo(1)
robotArm.moveTo(1)
robotArm.moveTo(8)
robotArm.getNextColorRight('green')
robotArm.drop()
robotArm.moveLeft()
robotArm.getNextColorLeft('red')

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()