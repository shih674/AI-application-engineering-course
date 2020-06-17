import colorama
import time

colorama.init()

red_light = colorama.Back.RED
yellow_light = colorama.Back.YELLOW
green_light = colorama.Back.GREEN

start = 1

while start < 30:
    if start%10 < 5:
        pointer = red_light
    else:
        if start%10 < 6:
            pointer = yellow_light
        else:
            pointer = green_light
    print(pointer,'\r\n',start,'\r',end = ' ')
    #print(f" ",end = ' ')
    time.sleep(1)

    start += 1


