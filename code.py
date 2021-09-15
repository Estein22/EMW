from adafruit_circuitplayground import cp

while True:
    if cp.button_a:
        cp.play_file("grub.wav")
    if cp.button_b:
        cp.play_file("git_good.wav")
