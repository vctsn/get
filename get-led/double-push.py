import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
num = 0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.2
while True:
    if GPIO.input(up):
        num = num + 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        num = num - 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(up) and GPIO.input(down):
        num = 255
    if num <= 0 or num > 2**8:
        GPIO.output(leds, 0)
    for i in range(len(dec2bin(num))):
        if dec2bin(num)[i] == 1:
            GPIO.output(leds[i], 1)
        else:
            GPIO.output(leds[i], 0)