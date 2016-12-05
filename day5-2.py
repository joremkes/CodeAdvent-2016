import hashlib, os

input = 'abbhdwsy'

pin = ['.', '.', '.', '.', '.', '.', '.', '.']

matches = 0
m = hashlib.md5()
counter = 0
os.system('cls' if os.name == 'nt' else 'clear')
print 'start decrypting'

while matches < 8:
    input_for_hash = input + str(counter)
    hashstr = hashlib.md5(input_for_hash).hexdigest()

    if hashstr[:5] == '00000':
        position = int(hashstr[5], 16)
        character = hashstr[6]
        if position < 8:
            if pin[position] == '.':
                os.system('cls' if os.name == 'nt' else 'clear')
                matches = matches + 1
                pin[position] = character
                for i in pin:
                    print i,
                print
                print 'decrypting' + '.' * matches

    counter+=1

print 'Pin is ' + ''.join(pin)
print 'Done!'
