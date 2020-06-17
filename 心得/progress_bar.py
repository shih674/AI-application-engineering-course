'''python version 3.7'''
import time
import random

def ProgressBar(now,totoal):
    symbol = '#'
    bar_length = 100
    percent = int(now/totoal*100)
    if percent > 100:
        percent = 100
    left_num = int(bar_length*percent/100)
    right_num = bar_length - left_num
    left  =  symbol * left_num
    right = '.' * right_num
    full = left + right
    print(f'\r[{full}] {percent}%',end='',flush=True)

total = random.randint(0,1000)
pointer = 0
while pointer < total:
    poison = random.randint(0,int(total/20))
    pointer = pointer + poison
    ProgressBar(pointer,total)
    time.sleep(0.2)