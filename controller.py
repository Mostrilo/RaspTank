
import movement 
import ultrasonic 
import time 
import random

def turn_left(degrees):
  movement.moveTank(100,100)
  time.sleep(.008888*degrees)
  movement.motorStop()

def turn_right(degrees):
  movement.moveTank(-100,-100)
  time.sleep(.008888*degrees)
  movement.motorStop()

def move_forward(seconds):
   movement.moveTank(-100,100)
   time.sleep(seconds)

def move_backwards(seconds):
   movement.moveTank(100,-100)
   time.sleep(seconds)

