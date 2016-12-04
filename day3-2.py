possible = 0
row = []
end = False

with open('data-day3-1.txt' , 'r') as f:
    while not end:
        row = []
        column = []
        for i in range(3):
            try:
                line = f.next()
                row.append(map(int, line.split()))
            except StopIteration:
                print 'End of file!'
                end = True
                break
        print 'row is gevuld'
        print row[0], row[1], row[2]

        for a in range(3):
            column = []
            for b in range(3):
                column.append(row[b][a])
            column.sort()
            print column
            if column[2] < (column[0] + column[1]):
                possible = possible + 1
                print possible
#        print row[0], row[1], row[2]
