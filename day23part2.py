with open("./aoc/2023/23/data.txt") as f:
    data = f.read().split("\n")
width,height = len(data[0]),len(data)
start, end = (1,0),(width-2,height-1)

walls = set()
walls.add((1,-1)) #so we dont go above
walls.add((width-2,height)) #so we dont go below
junctions = set()
for y in range(height):
    for x in range(width):
        if data[y][x] == "#":
            walls.add((x,y))
        else:
            neighbours = 0
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                if x+dx>-1 and y+dy>-1 and x+dx<width and y+dy<height:
                    if data[y+dy][x+dx] != "#":
                        neighbours += 1
            if neighbours > 2:
                junctions.add((x,y))
# print(junctions)
# print(len(junctions))
# exit()

#now find junction links
linkage = {}
junctions.add(start)
junctions.add(end)#probably
print(junctions)
for junction in junctions:
    linkage[junction] = {}
    #try all four directions
    for dx1,dy1 in ((1,0),(-1,0),(0,1),(0,-1)):
        #this will only apply once
        x,y = junction
        oldx,oldy = dx1,dy1
        if (x+dx1,y+dy1) not in walls: #try
            x+=dx1
            y+=dy1
            time = 1
            while True:
                if (x,y) in junctions:# and (x,y) != junction:
                    linkage[junction][(x,y)] = time
                    if junction == end:
                        lastjunk = (x,y)
                    break
                time += 1
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    if (x+dx,y+dy) not in walls and (dx,dy) != (-1*oldx,-1*oldy):
                        x,y,oldx,oldy = x+dx,y+dy,dx,dy
                        break


print(linkage)
print(lastjunk)
            


"""
DEPTH FIRST
go between junctions
if we run into lastjunk go straight to the end
"""
def getlengths(path):
    t=0
    # print(path)
    for p in range(len(path) - 1):
        t += linkage[path[p]][path[p+1]]
    return t


total = 0
paths=[[start]]
while paths != []:
    newpaths=[]
    for path in paths:
        node = path[-1]
        if node == end:
            length = getlengths(path)
            if length > total:
                total = length
                print(length)
        elif node == lastjunk:
            newpaths.append(path+[end])

        else:
            for dest in linkage[node]:
                if dest not in path:
                    newpaths.append(path+[dest])

    paths=[x for x in newpaths.copy()]

