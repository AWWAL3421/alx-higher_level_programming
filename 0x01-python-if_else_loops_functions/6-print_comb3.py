#!/usr/bin/python3
for c in range(0, 10):
    for y in range(c + 1, 10):
        if c == 8 and y == 9:
            print('89')
        else:
            print('{}{}, '.format(c, y), end='')

