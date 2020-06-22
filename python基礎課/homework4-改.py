import colorama
import time
import os

colorama.init()

red_light    = colorama.Back.RED
yellow_light = colorama.Back.YELLOW
green_light  = colorama.Back.GREEN

traffic_light = [[colorama.Back.YELLOW,1],
                 [colorama.Back.RED, 0], [colorama.Back.RED, 0], [colorama.Back.RED, 0], [colorama.Back.RED, 0], [colorama.Back.RED, 0],
                 [colorama.Back.GREEN, 2], [colorama.Back.GREEN, 2], [colorama.Back.GREEN, 2], [colorama.Back.GREEN, 2]]

start = 1
while True:
    os.system('cls')
    key = start % 10
    pointer, space = traffic_light[key]
    print('   '*space, pointer,'  ',colorama.Back.RESET )
    print(start)

    time.sleep(1)
    start += 1