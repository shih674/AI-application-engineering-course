import colorama
import time
import os

colorama.init()

red_light    = colorama.Back.RED
yellow_light = colorama.Back.YELLOW
green_light  = colorama.Back.GREEN

traffic_light = [colorama.Back.YELLOW,
                 colorama.Back.RED, colorama.Back.RED, colorama.Back.RED, colorama.Back.RED, colorama.Back.RED,
                 colorama.Back.GREEN, colorama.Back.GREEN, colorama.Back.GREEN, colorama.Back.GREEN]

start = 1
while True:
    os.system('cls')
    key = start % 10
    pointer = traffic_light[key]

    print(pointer,' ',colorama.Back.RESET )
    print(start)

    time.sleep(1)
    start += 1
