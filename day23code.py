with open("./aoc/2023/23/example.txt") as f:
    data = f.read().split("\n")
width,height = len(data[0]),len(data)
start, end = (1,0),(width-2,height-1)

walls = set()
walls.add((1,-1)) #so we dont go above
slopes = {}
for y in range(height):
    for x in range(width):
        if data[y][x] == "#":
            walls.add((x,y))
        elif data[y][x] != ".":
            slopes[(x,y)] = data[y][x]

time = 0
paths = [[start]]
while paths != []:
    # print(paths)
    newpaths = []
    time += 1
    for path in paths:
        if path[-1] == end:
            continue
        x,y = path[-1]
        #attempt to move
        if (x,y) not in slopes or slopes[(x,y)] == ">":
            if (x+1,y) not in path and (x+1,y) not in walls:
                newpaths.append(path+[(x+1,y)])
        if (x,y) not in slopes:
            if (x-1,y) not in path and (x-1,y) not in walls:
                newpaths.append(path+[(x-1,y)])

        if (x,y) not in slopes or slopes[(x,y)] == "v":
            if (x,y+1) not in path and (x,y+1) not in walls:
                newpaths.append(path+[(x,y+1)])

        if (x,y-1) not in path and (x,y-1) not in walls:
            newpaths.append(path+[(x,y-1)])
    paths = [x for x in newpaths.copy()]
print(time)