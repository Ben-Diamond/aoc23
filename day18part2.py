with open("./aoc/2023/18/data.txt") as f:
    data = [x.split(" ") for x in f.read().split("\n")]
# print(data)

# bounds = [0,0,0,0]
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
walls = []
x,y = 0,0

"""
if direction of vertical wall is the same as the next
vertical wall, remove the last tile


place all VERTICAL WALLS in order
for evert one - check all other vertical walls
if there is overlap, split right wall, split left wall, between corresponding segments is a rectangle
note if part of a wall is left/right, the entire wall must be left/right
if the overlap is of length 1, ignore


for the actual thing, we ||always store vertical lines, always in order of x value. pop each vertical line, 
look through other lines to find the first one to the right of it with overlap, pop that as well. 
increase total by the size of the rectangle they enclose. add the sections of those lines that are not part of the overlap, 
repeat until nothing left ||


uncomment things to make part 1 work or something
"""


def enqueue(q,w):
    if q == []:
        return [w]
    p=0
    while q[p]["x"] < w["x"]:
        p+=1
        if p == len(q):
            break
    q.insert(p,w)
    # print("q",q)
    return q

dx,dy = 0,0
# dirs = {"R":(1,0),"L":(-1,0),"U":(0,-1),"D":(0,1)}
dirs = [(1,0),(0,1),(-1,0),(0,-1)] #for real
inside = [False,False]
 #EXAMPLE PART 1 = FALSE FALSE
 #EXAMPLE PART 2 = FALSE FALSE
 #DATA PART 1 = TRUE FALSE
 #DATA PART 2 = FALSE FALSE

#106941819907437
#106941741440909
for l in range(len(data)):
    line = data[l]
    things = ((l-2)%len(data),(l-1)%len(data),l,(l+1)%len(data))
    # dx,dy = dirs[line[0]]
    dx,dy = dirs[int(line[2][-2])] #for real
    # length = int(line[1])
    length = int(line[2][2:-2], 16) #for real
    #-1 ????
    # if data[things[0]][0] == data[things[2]][0]:
    #     inside[0] = not inside[0]
    # if data[things[1]][0] == data[things[3]][0]:
    #     inside[1] = not inside[1]
    if data[things[0]][2][-2] == data[things[2]][2][-2]: #for real
        inside[0] = not inside[0]
    if data[things[1]][2][-2] == data[things[3]][2][-2]:
        inside[1] = not inside[1]

    if dx == 0:
        if dy == 1:#down
            # if inside:
            
                walls = enqueue(walls,{"x":x,"bottom":y+inside[0],"top":y+length-inside[1],"side":"left","done":False})
            # else:
                # walls = enqueue(walls,{"x":x,"bottom":y,"top":y+length,"side":"left","done":False})
        else:
            # if inside:
                walls = enqueue(walls,{"x":x,"bottom":y-length+inside[1],"top":y-inside[0],"side":"left","done":False})
            # else:
                # walls = enqueue(walls,{"x":x,"bottom":y-length,"top":y,"side":"left","done":False})
            # walls.append({"x":x,"bottom":y-length,"top":y,"side":"left"})
    x+=length*dx
    y+=length*dy
    #     bounds[2] = y
    # if y > bounds[3]:
    #     bounds[3] = y
print(walls)
def draw2(walls):
    out = ""
    for y in range(-333,61):
        for x in range(-70,201):
            flag = False
            for w in walls:
                if w["x"] == x and w["bottom"] <= y and w["top"] >= y:
                    flag = True
                    out += "#"
            if not flag:
                out += "."
        out += "\n"
    with open("./aoc/2023/18/drawing2.txt","w") as f:
        f.write(out)
def draw3(walls):
    out = ""
    #-914299
    for y in range(0,2000000,10000):
        for x in range(0,2000000,10000):
            
            flag = False
            for w in walls:
                if w["x"] < x+10000 and w["x"]>=x and w["bottom"] <= y and w["top"] >= y:
                    flag = True
                    out += "#"
            if not flag:
                out += "."
        out += "\n"
    with open("./aoc/2023/18/drawing3.txt","w") as f:
        f.write(out)

def check(w1,w2):
    if w1["top"] < w2["bottom"]:
        return False
    if w2["top"] < w1["bottom"]:
        return False
    return (max(w1["bottom"],w2["bottom"]),min(w2["top"],w1["top"]))
    

total = 0
# wallNum = 0
while True:
    wall = walls.pop(0)
    x,b,t,s,d = wall.values()
    
    if wall["done"] == True:
        continue
    if wall["side"] == "right":
        continue

    #look for possible right walls
    temp = 0
    print("wall is",wall)
    while not check(wall,walls[temp]):
        temp += 1
    wall2 = walls.pop(temp)
    x2,b2,t2,s2,d2 = wall2.values()
    #split wall and walls[temp]
    overlap = check(wall,wall2)
    total += (overlap[1]-overlap[0]+1)*(x2-x+1)
    if walls == []:
        print("le total",total)
    # print("aaaa",overlap,wall2)
    if overlap[0] > b:
        walls = enqueue(walls,{"x":x,"bottom":b,"top":overlap[0]-1,"side":"left","done":False})
    if overlap[1] < t: #add last half
        walls = enqueue(walls,{"x":x,"bottom":overlap[1]+1,"top":t,"side":"left","done":False})
    
    #add parts of the right wall that were not covered
    if overlap[0] > b2:
        walls = enqueue(walls,{"x":x2,"bottom":b2,"top":overlap[0]-1,"side":"right","done":False})
    
    if overlap[1] < t2:
        walls = enqueue(walls,{"x":x2,"bottom":overlap[1]+1,"top":t2,"side":"right","done":False})
