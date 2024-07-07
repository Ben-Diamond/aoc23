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
# print(sand)
# print(bricks)

def checkmove(x,y,z,b):
    # x,y,z = coords
    if z==1 or ((x,y,z-1) in sand and sand[x,y,z-1] != b):
        return False
    return True
#move them down

immobile = set()
while len(immobile) != len(bricks):
    for b, brick in enumerate(bricks):
        #move them all by one
        if b in immobile:
            continue
        for x,y,z in brick:
            if not checkmove(x,y,z,b):
                immobile.add(b)
        if b not in immobile:
            new = []
            for x,y,z in brick:
                new.append((x,y,z-1))
                sand.pop((x,y,z))
                sand[(x,y,z-1)] = b
            bricks[b] = new

expendables = set()
# print(bricks)
print(sand)
total = 0
for b,brick in enumerate(bricks):
    # print("brick",brick,b)
    #first find if this brick supports any others
    support = False
    for x,y,z in brick:
        if (x,y,z+1) in sand and sand[(x,y,z+1)] != b: #it supports something
            support = True
    if not support:
        # print("not support")
        expendables.add(b)

    #if exactly one thing supports it then that thing cannot go
    supporters = set()
    for x,y,z in brick:
        if (x,y,z-1) in sand and sand[(x,y,z-1)] != b:
            supporters.add(sand[(x,y,z-1)])
    print(supporters)
    if len(supporters) != 1:
        expendables = expendables.union(supporters)
# print(expendables)
print(len(expendables))