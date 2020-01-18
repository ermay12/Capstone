import robot;

def followLines():
  while(True):
    if(robot.lightSensor()):
      robot.turnLeft()
    else:
      robot.turnRight()
      
followLines()
