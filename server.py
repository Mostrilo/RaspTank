#import movement 
import ultrasonic 
#import time 
import random
import controller
#import speakers

#start = time.time()

while True:
    controller.open_hand()
    while ultrasonic.distance() > 0.4:
        #print(ultrasonic.distance())
        controller.move_forward(0.01)
    #left = bool(random.getrandbits(1))
    left = bool(random.getrandbits(1))
    controller.close_hand()
    if(left):
        while ultrasonic.distance() <= 0.7:
            controller.turn_left(130)
    else:
        while ultrasonic.distance() <= 0.7:
            controller.turn_right(130)

#controller.turn_right(130)
#controller.turn_right(90)
#

#controller.turn_right(90)
#movement.destroy()
#speakers.
#controller.turn_right(90)
#controller.turn_left(90)

