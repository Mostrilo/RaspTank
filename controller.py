
import movement 
import ultrasonic 
import time 
import random
import servos

def turn_left(degrees):
  movement.moveTank(100, -100)
  time.sleep(.008888 * degrees)
  movement.motorStop()

def turn_right(degrees):
  movement.moveTank(-100, 100)
  time.sleep(.008888 * degrees)
  movement.motorStop()

def move_forward(seconds):
   movement.moveTank(-100, 100)
   time.sleep(seconds)

def move_backwards(seconds):
   movement.moveTank(100, -100)
   time.sleep(seconds)

  
def open_hand(degrees=-10):
  servos.hand(degrees)
  time.sleep(.15)
  
def close_hand(degrees=7):
  servos.hand(degrees)

def move_arm(position):
  servo.arm_pos(position)
  time.sleep(.2)
  
def move_wrist(degrees):
  #-90 to 90 degrees
  servo.wrist(int((degrees/12)+6))
  time.sleep(.25)

