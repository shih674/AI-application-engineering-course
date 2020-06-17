import  time

a = 0
for i in range(2):
    while a < 10:
        b = a-1
        print(f'{a}',end= '...',flush=True)
        a += 1
        time.sleep(1)
    print('\n')