import max7219
from machine import Pin, SPI
from time import sleep
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)

ready = 'Ready?'
clear = 'Clear'
length = len(ready)
length = len(clear)

length = (length*12)
display = max7219.Matrix8x8(spi, ss, 4)
display.brightness(1)   # adjust brightness 1 to 15
display.fill(1)
display.show()
sleep(0.5)
display.fill(0)
display.show()
sleep(0.2)

bt1 = Pin(11, Pin.IN, Pin.PULL_UP)
bt2 = Pin(12, Pin.IN, Pin.PULL_UP)
bt3 = Pin(13, Pin.IN, Pin.PULL_UP)

# สร้างฟังก์ชันเริ่มการนับ
def start_counting(display, bt2, bt3):
    i = 0
    x = 0
    counting = True
    while counting:
        if not bt3.value():  # หยุดนับเมื่อกดปุ่ม B2
            counting = False
            break
        number_str = str(i)
        length = len(number_str)
        display.text(number_str, 0, 0, 1)
        display.show()
        sleep(0.15)
        display.text(number_str, 0, 0, 0)
        display.show()
        display.fill(0)
        i += 1
        x += 1
        if not bt2.value():  # หยุดนับเมื่อกดปุ่ม B2
            counting = False
            display.text(number_str, 0, 0, 0)
            display.stop()
            number_str2 = str(x)
            length = len(number_str2)
            display.text(number_str2, 0, 0, 1)
            display.show()
            display.stop()
            display.fill(0)
            while True:
                if not bt3.value():  # หยุดการแสดงผลเมื่อกดปุ่ม B3 อีกครั้ง
                    display.text(number_str2, 0, 0, 0)
                    display.show()
                    break

# ... โค้ดอื่น ๆ ...

# ในลูปหลัก
while True:
    B1 = bt1.value()
    B2 = bt2.value()
    B3 = bt3.value()
    
    if (B1 == 1) and (B2 == 1) and (B3 == 1):
        display.text(clear ,0,0,0)
        display.text(ready ,0,0,0)
    
    elif (B1 == 0) and (B2 == 1) and (B3 == 1):
        for x in range(32, -length, -1):
            display.text(ready ,x,0,1)
            display.show()
            sleep(0.05)
            display.fill(0)
                
    elif (B1 == 1) and (B2 == 0) and (B3 == 1):
        start_counting(display, bt2, bt3)
                
    elif (B1 == 1) and (B2 == 1) and (B3 == 0):
        for i in range(32, -length, -1):
            display.text(clear ,i,0,1)
            display.show()
            sleep(0.05)
            display.fill(0)
