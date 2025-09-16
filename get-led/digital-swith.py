import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT) 
bottom=13
GPIO.setup(bottom, GPIO.IN)
state = 0
while True:
    if GPIO.input(bottom):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)

        

