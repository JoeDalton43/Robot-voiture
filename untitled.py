print("HelloWorld")
import RPi.GPIO as GPIO
#import keyboard
import time
M1_En=21
M2_En=18
M1_IN1=20
M1_IN2=16
M2_IN1=23
M3_IN2=24
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(M1_IN1,GPIO.OUT,initial = GPIO.HIGH)

"""GPIO.setup(M1_IN2,GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(M1_En,GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(M2_IN1,GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(M3_IN2,GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(M2_En,GPIO.OUT,initial = GPIO.HIGH)"""



"""while True:
	GPIO.output(21,not GPIO.input(21))
	time.sleep(0.5)"""
