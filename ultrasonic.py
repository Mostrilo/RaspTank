#!/usr/bin/python3
# File name   : Ultrasonic.py
# Description : Detection distance and tracking with ultrasonic
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/10/12
import RPi.GPIO as GPIO
import time
#import Adafruit_PCA9685

Tr = 11
Ec = 8

#pwm = Adafruit_PCA9685()
#pwm.set_pwm_freq(50)

def distance():       #Reading distance
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)
    GPIO.output(Tr, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)
    tries = 0
    max_tries = 1000
    while not GPIO.input(Ec):
        if (tries == max_tries):
            return distance()
        tries+=1
    t1 = time.time()
 
    while GPIO.input(Ec):
        pass
    t2 = time.time()
    return (t2-t1)*340/2
