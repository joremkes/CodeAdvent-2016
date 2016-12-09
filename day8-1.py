import os, numpy, time

def printDisplay():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(rows):
        print ''.join(display[y])

file = open('data-day8-1.txt')
# initize display
rows = 6
columns = 50
pixels = 0
display = []

for y in range(rows):
    display.append([])
    for x in range(columns):
        display[y].append('.')
display = numpy.asarray(display)

for line in file:
    command = line.split()
    if command[0] == 'rect':
        x = int(command[1].split('x')[0])
        y = int(command[1].split('x')[1])
        for yy in range(y):
            for xx in range(x):
                display[yy][xx] = '#'

    elif command[0] == 'rotate' and command[1] == 'row':
        y = int(command[2][2:])
        amount = int(command[4])
        display[y] = numpy.roll(display[y], amount)

    elif command[0] == 'rotate' and command[1] == 'column':
        x = int(command[2][2:])
        amount = int(command[4])
        display[:, x] = numpy.roll(display[:, x], amount)
    else:
        continue

    printDisplay()
    time.sleep(0.05)

for i in range(rows):
    pixels = pixels + ''.join(display[i]).count('#')

print pixels
