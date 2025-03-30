import RPi.GPIO as GPIO
from multiprocessing import Process
GPIO.setmode(GPIO.BCM)

class photoresistor():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin,GPIO.IN)
    def _readLight(self):
        while True:
            print(GPIO.input(self.pin))
    def readLight(self):
        p = Process(target=self._readLight)
        p.run()
        p.join()
