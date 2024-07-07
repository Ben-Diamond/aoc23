with open("./aoc/2023/22/data.txt") as f:
    data = f.read().split("\n")
bricks = []
sand = {}


for l,line in enumerate(data):
    x1,y1,z1,x2,y2,z2 = [int(x) for x in line.replace("~",",").split(",")]
    brick = [(x1,y1,z1)]
    for x in range(x2-x1):
        brick.append((x1+x+1,y1,z1))
    for y in range(y2-y1):
        brick.append((x1,y1+y+1,z1))
    for z in range(z2-z1):
        brick.append((x1,y1,z1+z+1))
    z = 0
    while z < len(bricks) and bricks[z][0][2] < brick[0][2]:
        z+=1
    bricks.insert(z,brick)

    # bricks.append(brick)
for b in range(len(bricks)):
    for b2 in bricks[b]:
        sand[b2] = b
# ###print(sand)
# ###print(bricks)

def checkmove(coords,ignore=False):
    x,y,z = coords
    # ignore = True
    if z==1 or (x,y,z-1) in sand:
        # if ignore != False:
        #     if (x,y,z-1) in sand and sand[(x,y,z-1)] == ignore:
        #         return True
        return False
    return True
#move them down

for b in range(len(bricks)):

    brick = bricks[b]
    # for z in brick:
        # if sand[z] != b:
            ###print("???",z,b,sand[z])
    if len(brick) == 1 or brick[0][2] != brick[1][2]: #a stick
        while checkmove(brick[0]):
            x,y,z = brick[0]
            # ###print(brick)
            # exit()
            brick.insert(0,(x,y,z-1))
            sand[(x,y,z-1)] = b
            sand.pop(brick[-1])
            brick.pop(-1)
        bricks[b] = brick
    else:
        ok = True
        shift = -1
        while ok:
            shift += 1
            for x,y,z in brick:
                if not checkmove((x,y,z-shift)):
                    ok = False
                    break
            # if ok:
            #     shift += 1
            #     for c in range(len(brick)):
        # ###print("shift",shift)
        if shift!=0:
            for c in range(len(brick)):
                sand.pop(brick[c])
                brick[c] = (brick[c][0],brick[c][1],brick[c][2]-shift)
                sand[brick[c]] = b
            bricks[b] = brick
# exit()
##print(bricks)       

#now sort them
newbricks = []
newsand = {}
for b,brick in enumerate(bricks):
    z=0
    while z < len(newbricks) and newbricks[z][0][2] < brick[0][2]:
        z+=1
    newbricks.insert(z,brick)
for b, brick in enumerate(newbricks):
    for cube in brick:
        newsand[cube] = b
##print(bricks)
# exit()
#print(newsand)
#print(newbricks)
#now act as if delet
total = 0
for ignore in range(len(bricks)):
# ignore = 0
# if True:
    bricks = [c.copy() for c in newbricks]
    sand = newsand.copy()
    #print(bricks,">")
    for cube in bricks[ignore]:
        #print(cube)
        sand.pop(cube)
    bricks[ignore] = []
    #print(bricks)
    #print(sand)
    

    for b in range(len(bricks)):
        if b == ignore:
            continue

        brick = bricks[b]
        # for z in brick:
            # if sand[z] != b:
                ###print("???",z,b,sand[z])
        if len(brick) == 1 or brick[0][2] != brick[1][2]: #a stick
            moved = False
            while checkmove(brick[0],ignore):
                moved = True
                x,y,z = brick[0]
                # ###print(brick)
                # exit()
                brick.insert(0,(x,y,z-1))
                sand[(x,y,z-1)] = b
                sand.pop(brick[-1])
                brick.pop(-1)
            if moved:
                total += 1
            bricks[b] = brick
        else:
            ok = True
            shift = -1
            while ok:
                shift += 1
                for x,y,z in brick:
                    if not checkmove((x,y,z-shift),ignore):
                        ok = False
                        break
                # if ok:
                #     shift += 1
                #     for c in range(len(brick)):
            # ###print("shift",shift)
            if shift!=0:
                total += 1
                for c in range(len(brick)):
                    sand.pop(brick[c])
                    brick[c] = (brick[c][0],brick[c][1],brick[c][2]-shift)
                    sand[brick[c]] = b
                bricks[b] = brick
    print(total)