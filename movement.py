#!/usr/bin/env python3

# File name   : move[ment].py
# Description : Control Motor
# Product     : RaspTank
# Website     : /, www.adeept.com
# E-mail      : alexandermertens06@gmail.com, support@adeept.com
# Author      : Mesalcode, William
# Date        : 2020/9/27, 2018/12/27
# Forked from HoldenA1/RaspTank-lib by Mesalcode

import time
import math
import RPi.GPIO as GPIO

# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_A_EN    = 4
Motor_B_EN    = 17

Motor_A_Pin1  = 14
Motor_A_Pin2  = 15
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18

pwn_A = 0
pwm_B = 0

multiplier_left = 1
multiplier_right = -1

def motorStop():#Motor stops
	GPIO.output(Motor_A_Pin1, GPIO.LOW)
	GPIO.output(Motor_A_Pin2, GPIO.LOW)
	GPIO.output(Motor_B_Pin1, GPIO.LOW)
	GPIO.output(Motor_B_Pin2, GPIO.LOW)
	GPIO.output(Motor_A_EN, GPIO.LOW)
	GPIO.output(Motor_B_EN, GPIO.LOW)


def setup():#Motor initialization
	global pwm_A, pwm_B
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Motor_A_EN, GPIO.OUT)
	GPIO.setup(Motor_B_EN, GPIO.OUT)
	GPIO.setup(Motor_A_Pin1, GPIO.OUT)
	GPIO.setup(Motor_A_Pin2, GPIO.OUT)
	GPIO.setup(Motor_B_Pin1, GPIO.OUT)
	GPIO.setup(Motor_B_Pin2, GPIO.OUT)

	motorStop()
	try:
		pwm_A = GPIO.PWM(Motor_A_EN, 1000)
		pwm_B = GPIO.PWM(Motor_B_EN, 1000)
	except:
		pass


def moveRight(percentSpeed):#Motor 2 positive and negative rotation
	percentSpeed *= multiplier_right
	if percentSpeed == 0: # stop
		GPIO.output(Motor_B_Pin1, GPIO.LOW)
		GPIO.output(Motor_B_Pin2, GPIO.LOW)
		GPIO.output(Motor_B_EN, GPIO.LOW)
	else:
		if percentSpeed < 0:
			GPIO.output(Motor_B_Pin1, GPIO.HIGH)
			GPIO.output(Motor_B_Pin2, GPIO.LOW)
			pwm_B.start(100)
			pwm_B.ChangeDutyCycle(abs(percentSpeed) - 1)
		elif percentSpeed > 0:
			GPIO.output(Motor_B_Pin1, GPIO.LOW)
			GPIO.output(Motor_B_Pin2, GPIO.HIGH)
			pwm_B.start(0)
			pwm_B.ChangeDutyCycle(abs(percentSpeed) - 1)


def moveLeft(percentSpeed):#Motor 1 positive and negative rotation
	percentSpeed *= multiplier_left
	if percentSpeed == 0: # stop
		GPIO.output(Motor_A_Pin1, GPIO.LOW)
		GPIO.output(Motor_A_Pin2, GPIO.LOW)
		GPIO.output(Motor_A_EN, GPIO.LOW)
	else:
		if percentSpeed < 0:
			GPIO.output(Motor_A_Pin1, GPIO.HIGH)
			GPIO.output(Motor_A_Pin2, GPIO.LOW)
			pwm_A.start(100)
			pwm_A.ChangeDutyCycle(abs(percentSpeed) - 1)
		elif percentSpeed > 0:
			GPIO.output(Motor_A_Pin1, GPIO.LOW)
			GPIO.output(Motor_A_Pin2, GPIO.HIGH)
			pwm_A.start(0)
			pwm_A.ChangeDutyCycle(abs(percentSpeed) - 1)


def moveTank(rightSpeed, leftSpeed):
	moveRight(rightSpeed)
	moveLeft(leftSpeed)

def moveArcade(throttle, turnSpeed):
	throttle *= -1
	turnSpeed *= -1
	leftPower = turnSpeed - throttle
	rightPower = turnSpeed + throttle
	moveTank(leftPower, rightPower)

def destroy():
	motorStop()
	GPIO.cleanup()             # Release resource

try:
	setup()
except KeyboardInterrupt:
	destroy()
