import movement 
import ultrasonic 
import time 
import random
import controller

start = time.time()
while True:
    open_hand()
    while ultrasonic.distance() > 0.4:
        #print(ultrasonic.distance())
        controller.move_forward(0.01)
    left = bool(random.getrandbits(1))
    close_hand()
    if(left):
        controller.turn_left(90)
    else:
        controller.turn_right(90)
#controller.turn_right(90)
movement.destroy()
