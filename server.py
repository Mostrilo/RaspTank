import movement 
import ultrasonic 
import time 
import random
import controller

start = time.time()
while True:
    while ultrasonic.distance() > 0.4:
        #print(ultrasonic.distance())
        controller.move_forward(0.05)
    left = bool(random.getrandbits(1))
    if(left):
        controller.turn_left(90)
    else:
        controller.turn_right(90)
#controller.turn_right(90)
movement.destroy()
