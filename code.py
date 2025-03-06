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
total_loop_cycle = 3
counter = 0

# constants
PIN_5 = 5;
PIN_4 = 4;
PIN_3 = 3;

# setup
red_led = digitalio.DigitalInOut(board.GP11)
blue_led = digitalio.DigitalInOut(board.GP13)
green_led = digitalio.DigitalInOut(board.GP12)
red_led.direction = digitalio.Direction.OUTPUT
blue_led.direction = digitalio.Direction.OUTPUT
green_led.direction = digitalio.Direction.OUTPUT

# arrays
pin = [red_led, green_led, blue_led]

# loop
while True:
    for counter in range(total_loop_cycle):

        # turns off previous light
        if for_loop_start > 0:
            pin[for_loop_start - 1].value = False

        if for_loop_start >= 0:
            pin[for_loop_start].value = True

        # Makes each loop one less than the last until it resets
        for_loop_start += 1

        for pin_select in range(for_loop_start, total_loop_cycle):
            pin[pin_select].value = True
            time.sleep(blink_delay) # Wait for 1000 millisecond(s)
            pin[pin_select].value = False
    

    # reset
    for_loop_start = -1
    counter = 0

    # white light
    red_led.value = True
    blue_led.value = True
    green_led.value = True
    time.sleep(blink_delay) # Wait for 1000 millisecond(s)
    red_led.value = False
    blue_led.value = False
    green_led.value = False

