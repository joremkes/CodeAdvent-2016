file = open('data-day7-1.txt')
total_valid_ips = 0

def testAbba(data):
    part = ''
    abba_found = False
    for i in range(len(data)-3):
        part = data[i:i+4]
        if part[0] == part[3] and part[1] == part[2] and part[0] != part [1]:
            abba_found = True
    if abba_found == True:
        return True
    else:
        return False

for line in file:
    ipv7_address = line.replace('[', ' ').replace(']',' ').split()
    true_or_not = []
    valid = False

    for s in ipv7_address:
        true_or_not.append(testAbba(s))


    for i in range(0, len(true_or_not),2):
        if true_or_not[i] == True:
            valid = True
    for i in range(1, len(true_or_not), 2):
        if true_or_not[i] == True:
            valid = False
    if valid:
        total_valid_ips = total_valid_ips + 1


print total_valid_ips
