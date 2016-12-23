puzzle = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 18 c
cpy 11 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

commands = puzzle.split('\n')

max_instructions = len(commands)

c = 1
registers = ['a', 'b', 'c', 'd']
register = [0,0,c,0]
i = 0

while i < max_instructions:
    command = commands[i].split()
    if command[0] == 'cpy':
        if command[1] in registers:
            register[ord(command[2])-97] = register[ord(command[1])-97]
        else:
            register[ord(command[2])-97] = int(command[1])
        i = i + 1

    elif command[0] == 'inc':
        register[ord(command[1])-97] = register[ord(command[1])-97] + 1
        i = i + 1

    elif command[0] == 'dec':
        register[ord(command[1])-97] = register[ord(command[1])-97] - 1
        i = i + 1

    elif command[0] == 'jnz':
        if command[1] in registers:
            if register[ord(command[1])-97] != 0:
                i = i + int(command[2])
            else:
                i = i + 1
        else:
            if int(command[1]) != 0:
                i = i + int(command[2])
            else:
                i = i + 1

print register[0]
