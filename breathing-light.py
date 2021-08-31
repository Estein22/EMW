import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

ramp_time = 5 # Time to ramp up, in seconds
period = 0.01  # Time per cycle, in seconds
step = period / ramp_time  # how much to increment the brightness each cycle

while True:
    brightness = 0
    while brightness < 1:
        T_on = brightness * period
        T_off = period - T_on
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
        brightness += step
    brightness = 1
    while brightness > 0:
        T_on = brightness * period
        T_off = period - T_on
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
        brightness -= step

