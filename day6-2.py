import string

file = open('data-day6.txt')

counter = 0
code = ''
data = []
column = []
letters_in_column = {}

for line in file:
    data.append(list(line))

for x in range(len(data[0])-1): # -i for return (\n) as last character
    column_list = []
    for y in range(len(data)):
        column_list.append(data[y][x])
    column.append(''.join(column_list))

for s in column:
    for l in string.ascii_lowercase:
        if l in s:
            letters_in_column[l] = s.count(l)

    hit = False

    for i in range(len(s)):
        for l in string.ascii_lowercase:
            if (l in letters_in_column.keys()) and (letters_in_column[l] == i) and not hit:
                hit = True
                code = code + l

print code
