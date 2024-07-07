with open("./aoc/2023/16/data.txt") as f:
    data = f.read().split("\n")
#print(data)
width,height = len(data[0]),len(data)

result = set()
states = set()
#print(result)
paths = [(0,0,0,1)]
while len(paths) > 0:
    newpaths = []
    for path in paths:
        # print(path)
        if path in states:
            print("already")
            continue
        x,y,dx,dy = path
        states.add(path)
        result.add((x,y))
        if x + dx == width or x + dx == -1 or y + dy == height or y + dy == -1:
        #end
            continue
        new = data[y+dy][x+dx]
        #print(new)
        if new == ".":
            #yeah
            newpaths.append((x+dx,y+dy,dx,dy))

        elif new == "|":
            if dy == 0:
                #split
                #print("split up and down")
                newpaths.append((x+dx,y+dy,0,1))
                #print("now up")
                newpaths.append((x+dx,y+dy,0,-1))
            else:
                newpaths.append((x+dx,y+dy,dx,dy))
            
        elif new == "-":
            if dx == 0:
                #split
                #print("split across")
                newpaths.append((x+dx,y+dy,1,0))
                #print("now left")
                newpaths.append((x+dx,y+dy,-1,0))
            else:
                newpaths.append((x+dx,y+dy,dx,dy))
            #split
        elif new == "\\":
            #print("so it works ig")
        #   \ turns (dx,dy) from ___ into ___
        # (1,0) into (0,1)
        # (-1,0) into (0,-1)
        # (0,1) into (1,0)
        # (0,-1) into (-1,0)
            #again with swapped dx and dy
            newpaths.append((x+dx,y+dy,dy,dx))
            pass
        elif new == "/":
        #   / turns (dx,dy) from ___ into ___
        # (1,0) into (0,-1)
        # (-1,0) into (0,1)
        # (0,1) into (-1,0)
        # (0,-1) into (1,0)
            #again with dx,dy = -dx, -dy
            newpaths.append((x+dx,y+dy,-1*dy,-1*dx))
    paths = newpaths.copy()
print(result,len(result))
def draw(result,data):
    out = ""
    for y in range(height):
        for x in range(width):
            if (x,y) in result:
                out += "#"
            else:
                out += data[y][x]
        out += "\n"
    with open("./aoc/2023/16/drawing.txt","w") as f:
        f.write(out)
draw(result,data)