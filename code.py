from adafruit_circuitplayground import cp
import time

while True:
    if cp.button_a:
        cp.play_file("Shulk.wav")
    if cp.button_b:
        cp.play_file("Shulk_B.wav")
# What happens when you push a button?
# What is the purpose of line 12?
# What is the mathematical operation happening on line 13?
# What does the while loop on lines 15-16 do?
# Can you make button b do something?
