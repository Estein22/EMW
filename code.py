import time
import random
from adafruit_circuitplayground import cp

# They are very bright, maybe keep them dim so they're easier to look at
cp.pixels.brightness = 0.05

time_step = 0.3  # time between turning on pixels
color = (0, 128, 0)
while True:
    for i in [0, 6, 2, 8, 4]:
        cp.pixels[i] = color
    time.sleep(time_step)
    for i in [0, 6, 2, 8, 4]:
        cp.pixels[i] = (0, 0, 0)
    for i in [1, 3, 5, 7, 9]:
        cp.pixels[i] = color
    time.sleep(time_step)
    for i in [1, 3, 5, 7, 9]:
        cp.pixels[i] = (0, 0, 0)
