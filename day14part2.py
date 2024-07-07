with open("./aoc/2023/14/data.txt") as f:
    data = f.read().split("\n")
cubes = set()
spheres = set()
width,height = len(data[0]),len(data)
for y in range(height):
    for x in range(width):
        if data[y][x] == "#":
            cubes.add((x,y))
        elif data[y][x] == "O":
            spheres.add((x,y))
# x,y coordinates!!!

def draw(cubes,spheres):

    with open("./aoc/2023/14/map.txt","a") as f:
        out = "\n"
        for y in range(height):
            for x in range(width):
                if (x,y) in cubes:
                    out += "#"
                elif (x,y) in spheres:
                    out += "O"
                else:
                    out += "."
            out += "\n"
        f.write(out)

def move(dx,dy,x,y,newSpheres):
    while (x+dx,y+dy) not in cubes and x+dx < width and x+dx>=0 and y+dy < height and y+dy>=0:
        x += dx
        y += dy
    while (x,y) in newSpheres: #backtrack
        # print("h")
        x -= dx
        y -= dy
    return (x,y)

def thing(spheres):
    for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)]:
        newSpheres = set()
        for sphere in spheres:
            new = move(dx,dy,sphere[0],sphere[1],newSpheres)
            newSpheres.add(new)
            # print(newSpheres)
        spheres = newSpheres
    return spheres
states = []
l = 0
looped = False
while l < 1000000000:
# while l < 3:
    total = 0
    spheres = thing(spheres)

    total = 0
    for s in spheres:
    # print(s)
        total += height - s[1]
    print(total,"num is",l)
    if False and not looped:
        states.append(spheres)
        for g in range(l-1):
            if states[g] == spheres:
                # [2], 9
                length = l - g
                print("loop",g,"length is",length)
                # while l + length < 1000000000:
                #     l += length
                    
                # num = 1000000000 - length + (1000000000 - g) % length
                num = length *(1000000000 // length)
                print("num",num)
                l = num - 1
                looped = True
                break
    if l == 80:
        l = 999999971
    # if l == 9:
    #     l = 999999989
    l += 1
# 80 + 17k = 1000000000
# 1000000000 - 80
total = 0
for s in spheres:
    # print(s)
    total += height - s[1]
print(total)
draw(cubes,spheres)
#100071 too hight
#not 100047
# 100064?