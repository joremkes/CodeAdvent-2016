possible = 0

file = open('data-day3-1.txt')

for line in file:
    sides = map(int, line.split())
    sides.sort()
    if sides[2] < (sides[0] + sides[1]):
        possible = possible + 1

print possible
