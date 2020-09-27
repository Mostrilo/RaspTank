import movement
import ultrasonic
import time

movement.moveArcade(10, 20)

time.sleep(1)

movement.moveTank(10, 10)

print(ultrasonic.distance())