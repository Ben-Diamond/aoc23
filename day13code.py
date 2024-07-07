with open("./aoc/2023/13/data.txt") as f:
    data = [x.split("\n") for x in f.read().split("\n\n")]
#print(data)
"""

#.##..##. .##..##.#
..#.##.#. .#.##.#..
##......# #......##
##......# #......##
..#.##.#. ..#.##.#.
..##..##. ..##..##.
#.#.##.#. #.#.#.#.#

"""

def checkRow(rocks,i): #AFTER i
    i2 = i + 1
    #print(i,i2)
    width = min(i+1,len(rocks[0]) - i2)
    if width == 0:
        return False
    print("width is",width,"for",i)
    for x in range(len(rocks)):
        for rock in range(width):
            if rocks[x][rock + i2] != rocks[x][i - rock]:#maybe
                # #print("bad",i)
                return False
    return True

def checkColumn(rocks,i): #AFTER i
    i2 = i + 1
    #print(i,i2) 
    height = min(i+1,len(rocks) - i2)
    if height == 0:
        return False
    #print("width is",height,"for",i)
    for x in range(height):
        for rock in range(len(rocks[x])):
            #print(x+i2,i-x,x,rocks[x+i2],rocks[i-x])
            if rocks[x + i2][rock] != rocks[i - x][rock]:#maybe
                # #print("bad",i)
                return False
    return True
total = 0

for line in data:
    #print("line")
    b = False
    print(b)
    for g in range(len(line[0])):
        if checkRow(line,g):
            print("column",g,line)
            total += g + 1
            b = True
            # break
    if b == False:
        pass

    for g in range(len(line)):
        if checkColumn(line,g):
            #print("row",g,line)
            total += (g+1)*100
            # breakS
print(total)
#29001 too high