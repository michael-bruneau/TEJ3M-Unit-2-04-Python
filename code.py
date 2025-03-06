# Created by: Michael Bruneau
# Created on: March 2025
#
# This module is a Raspberrypy Pico program that causes a RGB LED to change colours

import board
import digitalio
import time
import busio

# varaibles
blink_delay = 1
voltage_output = 0;
for_loop_start = -1
total_loop_cycle = 2
counter = 0

# constants
PIN_5 = 5;
PIN_4 = 4;
PIN_3 = 3;

# arrays
pin = [PIN_5, PIN_3, PIN_4]

# setup
led = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

# loop
while True:
    # turns on LED and pauses for one second
    led.value = True
    time.sleep(blink_delay)

    # turns off LED and pauses for one second
    led.value = False
    time.sleep(blink_delay)