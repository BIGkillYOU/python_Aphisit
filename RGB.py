from machine import Pin
import time

R = Pin(2, Pin.OUT)
G = Pin(3, Pin.OUT)
B = Pin(4, Pin.OUT)
B1 = Pin(6, Pin.IN, Pin.PULL_UP)
B2 = Pin(7, Pin.IN, Pin.PULL_UP)
B3 = Pin(8, Pin.IN, Pin.PULL_UP)

def RGBBT():
    while True:
        B11 = B1.value()
        B22 = B2.value()
        B33 = B3.value()

        if B11 == 0:
            print("R")
            R.value(1)
            G.value(0)
            B.value(0)
        elif B22 == 0:
            print("G")
            R.value(0)
            G.value(1)
            B.value(0)
        elif B33 == 0:
            print("B")
            R.value(0)
            G.value(0)
            B.value(1)
        else:
            print("OOO")
            R.value(0)
            G.value(0)
            B.value(0)

        time.sleep(0.1)
        
RGBBT()