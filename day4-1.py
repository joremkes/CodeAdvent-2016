import string
from operator import itemgetter
from collections import OrderedDict

sum_of_sectorid = 0

file = open('data-day4.txt')

for line in file:
    x = line.split('-')
    y = x[-1].split('[')
    name = ''.join(x[:-1])
    sectorid = int(y[0])
    checksum = y[1][:-2]

    #print name, sectorid, checksum

    letters_in_name = {}
    generated_checksum = ''

    #create dictionary with the amount of letters
    for l in string.ascii_lowercase:
        if l in name:
            letters_in_name[l] = name.count(l)

    #
    for i in range(len(name), 0, -1):
        for l in string.ascii_lowercase:
            if l in letters_in_name.keys():
                if letters_in_name[l] == i:
                    generated_checksum = generated_checksum + l

    if generated_checksum[:5] == checksum:
        sum_of_sectorid = sum_of_sectorid + sectorid

print sum_of_sectorid
