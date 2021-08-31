import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
short = 0.3
long = 1
while True:
    led.value = False
    time.sleep(1.5)
    led.value = True
    time.sleep(0.3)
    led.value = False
    time.sleep(1)
    for _ in range(0,3,1):
        led.value = True
        time.sleep(long)
        led.value = False
        time.sleep(short)
    led.value = True
    time.sleep(short)
    led.value = False
    time.sleep(1)
    for _ in range(0,4,1):
        led.value = True
        time.sleep(long)
        led.value = False
        time.sleep(1)
    led.value = False
    time.sleep(1)
    for _ in range(0,3,1):
        led.value = True
        time.sleep(long)
        led.value = False
        time.sleep(1)
    led.value = True
    time.sleep(short)

