file = open('data-day7-1.txt')
total_valid_ips = 0
part = ''

for line in file:
    ipv7_address = line.replace('[', ' ').replace(']',' ').split()
    aba = []
    aba_found = False
    bab = []
    bab_found = False

    for i in range(0, len(ipv7_address),2): # even, supernets
        data = ipv7_address[i]
        for j in range(len(data)-2):
            part = data[j:j+3]
            if part[0] == part[2] and part[0] != part [1]:
                aba.append(part)
                aba_found = True

    for i in range(1, len(ipv7_address), 2): # odd, hypernet
        data = ipv7_address[i]
        for j in range(len(data)-2):
            part = data[j:j+3]
            if part[0] == part[2] and part[0] != part [1]:
                bab.append(part)
                bab_found = True

    for i in range(len(aba)):
        if aba[i][1] + aba[i][0] + aba[i][1] in bab:
            total_valid_ips = total_valid_ips + 1
            break

print total_valid_ips
