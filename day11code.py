with open("./aoc/2023/11/data.txt") as f:
    data = f.read().split("\n")
print(data)
#nC2 = n(n-1)/2
emptyY = {y: True for y in range(len(data))}
emptyX = {x : True for x in range(len(data[0]))}
print(emptyX)
galaxies = []
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            emptyX[x] = False
            emptyY[y] = False
            galaxies.append((x,y))

def expansions(v1,v2,empties,scale):
    out = 0
    if v1 < v2:
        for x in range(v1,v2):
            if empties[x] == True:
                out += scale
    else:
        for x in range(v2,v1):
            if empties[x] == True:
                out += scale
    return out
# print(expansions(0,3,emptyX,1))

# exit()
total = 0
for x1,y1 in galaxies:
    # print("from",x1,y1)S
    for x2,y2 in galaxies:
        if x2 > x1 or (x2 == x1 and y2 > y1): #just to avoid double counting
            distance = abs(x2 - x1) + abs(y2 - y1) + expansions(x1,x2,emptyX,1000000-1) + expansions(y1,y2,emptyY,1000000-1)
            # print(f"to ({x2},{y2}); horizontally {abs(x2 - x1)} vertically {abs(y2 - y1)} expansions {expansions(x1,x2,emptyX,1)}, {expansions(y1,y2,emptyY,1)} total {distance}")
            total += distance


print(total)
    # exit()