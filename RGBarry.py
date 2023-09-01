from machine import Pin
import time

# Define RGB LED pins
led_pins = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT)]

# Define button pins with pull-up resistors
button_pins = [Pin(6, Pin.IN, Pin.PULL_UP), Pin(7, Pin.IN, Pin.PULL_UP), Pin(8, Pin.IN, Pin.PULL_UP)]

def set_color(red, green, blue):
    # Set the RGB 
    for i, pin in enumerate(led_pins):
        pin.value((i == 0 and red) or (i == 1 and green) or (i == 2 and blue))

def RGBBT():
    while True:
        # Read the state of the button pins and store in an array
        button_states = [button_pin.value() for button_pin in button_pins]

        # Check which button is pressed and set the RGB LED accordingly
        if button_states[0] == 0:
            print("R")
            set_color(0, 1, 0)  # Red
        elif button_states[1] == 0:
            print("G")
            set_color(0, 0, 1)  # Green
        elif button_states[2] == 0:
            print("B")
            set_color(1, 0, 0)  # Blue
        else:
            print("OOO")
            set_color(0, 0, 0)  # Off

        time.sleep(0.1)

RGBBT()