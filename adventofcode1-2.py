exercise = "L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2"
#exercise = "R8, R4, R4, R8"

route = []
stops = []
command = ''
richting = 'n'
draai = ''
stap = 0
x = 0
y = 0

# for i in range(len(exercise)):
#     letter = exercise[i]
#     if letter == " ":
#         continue
#     elif letter == ',':
#         route.append(command)
#         command = ''
#     else:
#         command = command + letter
# 
# route.append(command)

route = exercise.split(', ')

def update_positie(a,b,c):
    global x
    global y
    global stops
    for i in range(1, c+1):
        x = x + a
        y = y + b
        if [x,y] in stops:
            print 'Found! Answer is ' + str(abs(x) + abs(y))        
        stops.append([x,y])
        
        

for i in route:
    draai = i[0]
    stap = int(i[1:])
    
    if draai == 'L':
        if richting == 'n':
            richting = 'w'
            #x = x - stap
            update_positie(-1, 0, stap)
        elif richting == 'o':
            richting = 'n'
            #y = y + stap
            update_positie(0, 1, stap)
        elif richting == 'z':
            richting = 'o'
            #x = x + stap
            update_positie(1, 0, stap)
        elif richting == 'w':
            richting = 'z'
            #y = y - stap
            update_positie(0, -1, stap)
            
    if draai == 'R':
        if richting == 'n':
            richting = 'o'
            #x = x + stap
            update_positie(1, 0, stap)
        elif richting == 'o':
            richting = 'z'
            #y = y - stap
            update_positie(0, -1, stap)
        elif richting == 'z':
            richting = 'w'
            #x = x - stap
            update_positie(-1, 0, stap)
        elif richting == 'w':
            richting = 'n'
            #y = y + stap
            update_positie(0, 1, stap)
	
print 'Done!'
       