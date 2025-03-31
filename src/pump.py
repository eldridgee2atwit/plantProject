import RPi.GPIO as gpio
from time import sleep

class pump():
    def __init__(self, pin=18):
        self.pin=pin
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.OUT)
        gpio.output(self.pin,gpio.LOW)
    
    def water(self):
        gpio.output(self.pin,gpio.HIGH)
        sleep(1.5)
        gpio.output(self.pin, gpio.LOW)
        return
        