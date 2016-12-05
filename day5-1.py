import hashlib

input = 'abbhdwsy'

pin = ''

matches = 0
m = hashlib.md5()
counter = 0

while matches < 8:
    input_for_hash = input + str(counter)
    hashstr = hashlib.md5(input_for_hash).hexdigest()

    if hashstr[:5] == '00000':
        print input_for_hash, hashstr
        pin = pin + hashstr[5]
        matches+=1

    counter+=1

print pin
