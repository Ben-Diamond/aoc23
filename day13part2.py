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
    error = 0
    i2 = i + 1
    #print(i,i2)
    width = min(i+1,len(rocks[0]) - i2)
    if width == 0:
        return False
    # print("width is",width,"for",i)
    for x in range(len(rocks)):
        for rock in range(width):
            if rocks[x][rock + i2] != rocks[x][i - rock]:#maybe
                if error != 0:
                    return False
                # #print("bad",i)
                error = 1
    if error == 1:
        return True

def checkColumn(rocks,i): #AFTER i
    error = 0
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
                if error != 0:
                # #print("bad",i)
                    return False
                error = 1
    if error == 1:
        return True
total = 0
import time
s=time.time()
for line in data:
    for g in range(len(line[0])):
        if checkRow(line,g):
            total += g + 1
            break

    for g in range(len(line)):
        if checkColumn(line,g):
            total += (g+1)*100
            break
print(total)
print(time.time() - s)