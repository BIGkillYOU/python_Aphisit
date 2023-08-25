from machine import Pin, Timer
from time import sleep

led = Pin(25,Pin.OUT)
led1 = Pin(2,Pin.OUT)
led2 = Pin(3,Pin.OUT)
led3 = Pin(4,Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()
    led1.toggle()
    led2.toggle()
    led3.toggle()
    
#timer.init(freq=2.5,mode=Timer.PERIODIC,callback=blink)

def ledrun():
    LED234 = [Pin(2,Pin.OUT),Pin(3,Pin.OUT),Pin(4,Pin.OUT)]

    #while True:
    while 0==0:
        
        for i in LED234:
            i.on()
            sleep(0.5)
        #for LED in LEDS:
            i.off()
            sleep(0.5)
ledrun()