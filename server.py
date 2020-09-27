import movement 
import ultrasonic 
import time 
import random
import controller

start = time.time()
while True:
    controller.open_hand()
    while ultrasonic.distance() > 0.4:
        #print(ultrasonic.distance())
        controller.move_forward(0.01)
    #left = bool(random.getrandbits(1))
    left = True
    controller.close_hand()
    if(left):
        controller.turn_left(150)
    else:
        controller.turn_right(150)
#controller.turn_right(90)
movement.destroy()
