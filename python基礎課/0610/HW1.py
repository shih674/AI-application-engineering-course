print('='*15)

for i in range(1,10):
    for j in range(0,10):
        result = i * j
        if result < 10:
            result = ' ' + str(result)
        print(f'  {i} x {j} = {result}')
    if i != 9:
        print(' '+ '='*11)

print('='*15)

#============================================================
space = 5
for i in range(1,10):
    row = ''
    for j in range(1,10):
        result = i * j
        length = len(str(result))
        if length < space:
            result = ' ' * (space-length) + str(result)
        row = row + str(result)
    print(row)