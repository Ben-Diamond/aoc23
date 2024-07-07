with open("./aoc/2023/18/example.txt") as f:
    data = [x.split(" ") for x in f.read().split("\n")]
# print(data)

bounds = [0,0,0,0]
def draw(result,result2=[]):
    out = "\n"
    for y in range(bounds[2]-1,bounds[3]+1):
        for x in range(bounds[0]-1,bounds[1]+1):
            if (x,y) in result or (x,y) in result2:
                out += "#"
            else:
                out += "."
                # out += data[y][x]
        out += "\n"
    
    with open("./aoc/2023/18/drawing.txt","w") as f:
        f.write(out)
dirs = {"R":(1,0),"L":(-1,0),"U":(0,-1),"D":(0,1)}
walls = set()
x,y = 0,0
for line in data:
    dx,dy = dirs[line[0]]
    for p in range(int(line[1])):
        walls.add((x,y))
        x += dx
        y += dy
        if x < bounds[0]:
            bounds[0] = x
        if x > bounds[1]:
            bounds[1] = x
        if y < bounds[2]:
            bounds[2] = y
        if y > bounds[3]:
            bounds[3] = y


"""
TRAVERSAL
note all # are "in" but "state" is either "in" or "out"
if we reach # with # either side, state will flip
if we reach # with # on one side, we are at the start/end of a vertical wall
if the wall finishes with # on a different side to how it started, state will flip
note if a wall starts it should not end with # either side
"""

total = 0
inside = set()
for x in range(bounds[0],bounds[1]+1):
    state = 0
    tent = None
    for y in range(bounds[2],bounds[3]+1):

        if (x,y) in walls:
            total += 1
            inside.add((x,y))
            if (x-1,y) in walls:
                if (x+1,y) in walls: #we are entering the middle of a horizontal wall
                    state = 1 - state #flip
                else: #the right side of a horizontal wall - the top or bottom of a vertical wall
                    if tent == "right": #we started on the right: we are as before
                        pass
                    elif tent == "left": #we started on the left: we flip
                        state = 1 - state
                    else: #start of the wall
                        tent = "right"
            elif (x+1,y) in walls: #on the left
                if tent == "right": #we started on the right: we flip
                    state = 1 - state
                elif tent == "left": #we started on the left: we flip
                    pass
                else: #start of the wall
                    tent = "left"
        else:
            total += state
            if state == 1:
                inside.add((x,y))



print(bounds)
# print(inside)
draw(walls,inside)
print(total)