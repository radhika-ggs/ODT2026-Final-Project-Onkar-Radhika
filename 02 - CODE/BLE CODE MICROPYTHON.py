# Import Everything
from ble_keyboard import BLEKeyboard
from machine import Pin, TouchPad
import time

# Touch pads intialize
pads = [
    TouchPad(Pin(32)),
    TouchPad(Pin(4)),
    TouchPad(Pin(14)),
    TouchPad(Pin(12)),
    TouchPad(Pin(13)),
    TouchPad(Pin(33))
]
# define touch limits and keys from the BLE library
limits = [200, 200, 200, 200, 180, 200]
keys = [30, 31, 32, 33, 34, 35]
# define keyboard
kb = BLEKeyboard("radishkb")
# check for connection
print("Waiting for connection to radishkb keyboard")
while not kb.is_connected():
    pass
print("connected")

# debounce tracking
last_trigger = [0]*6
cooldown = 200  #set based on user testing

# smoothing function to provide average value of 3 readings to avoid spam.
#We added this to make the game fairer and more accurate to touch.
def read_filtered(touchpad, samples=3):
    total = 0
    for _ in range(samples):
        total += touchpad.read()
    return total // samples

while True:
    now = time.ticks_ms()
    #cycle through touchpads
    for i in range(6):
        #call smoothing function for each touchpad
        val = read_filtered(pads[i])
        # key trigger mechanism and cooldown checker. I did this to not do time.sleep() every time. Its proven to be more optimised
        if val < limits[i]: 
            if time.ticks_diff(now, last_trigger[i]) > cooldown:
                kb.send_raw(keys[i])
                last_trigger[i] = now 
                
                
                
                
                