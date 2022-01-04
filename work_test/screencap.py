import os
from time import sleep
for i in range(1, 50):
    sleep(0.1)
    os.system(f"adb shell screencap /sdcard/Pictures/Screenshot/screen{i}.png\n")

