import time
from adafruit_circuitplayground import cp

# They are very bright, maybe keep them dim so they're easier to look at
cp.pixels.brightness = 0.05

time_step1 = 0.3  # time between turning on pixels
time_step2 = 0.45
color1 = (128, 128, 128)
color2 = (0, 128, 0)
blank = (0, 0, 0)
while True:
    n = 10
    s = n

    while s > -10:
        print(s)
        for i in range(s):
            cp.pixels[i] = color1
            time.sleep(time_step1)
            cp.pixels[i] = blank
            s = s - 1
        n = n - 1
        s = n
        cp.pixels[n] = color2
        time.sleep(time_step2)
        cp.pixels[n] = color1
    # ^circle thing^

    n = 2
    while n > 0:
        for i in [0, 6, 2, 8, 4]:
            cp.pixels[i] = color2
        time.sleep(time_step1)
        for i in [0, 6, 2, 8, 4]:
            cp.pixels[i] = color1
        for i in [1, 3, 5, 7, 9]:
            cp.pixels[i] = color2
        time.sleep(time_step1)
        for i in [1, 3, 5, 7, 9]:
            cp.pixels[i] = color1
        n = n - 1
    time.sleep(time_step1)
    # ^altenation^

    n = 2
    while n > 0:
        for i in range(10):
            cp.pixels[i] = color2
        time.sleep(time_step1)
        for i in range(10):
            cp.pixels[i] = color1
        time.sleep(time_step1)
        n = n - 1
    # ^green flash^

    for i in range(10):
        cp.pixels[i] = blank

