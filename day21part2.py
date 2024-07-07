with open("./aoc/2023/21/example.txt") as f:
    data = f.read().split("\n")
# print(data)
width = len(data[0])
height = len(data)

walls = set()
for y in range(height):
    for x in range(width):
        if data[y][x] == "#":
            walls.add((x,y))
        elif data[y][x] == "S":
            start = (x,y)

#1,5,11,55

# def draw():
#     out = ""
#     for y in range(height):
#         for x in range(width):
#             if (x,y) in walls:
#                 out+="#"
#             elif (x,y) in visited:
#                 out+="O"
#             else:
#                 out+="."
#         out+="\n"
#     with open("./aoc/2023/21/drawing2.txt","w") as f:
#         f.write(out[:-1])
def draw():
    out = ""
    for y in range(-198,198):
        for x in range(-198,198):
            if (x%width,y%height) in walls:
                out+="#"
            elif (x,y) in visited:
                out+="O"
            else:
                out+="."
        out+="\n"
    with open("./aoc/2023/21/drawing2.txt","w") as f:
        f.write(out[:-1])
    


visited = set()
visited.add(start)

"""
range is from start-loop to start+loop in both directions (unsurprisingly)
start[0] = start[1]
width = height = 2*start + 1
"""

queue = [start]
for loop in range(100):
    newqueue = []
    for x,y in queue:
        #attempt to move twice
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            new = (x+dx,y+dy)
            new2 = ((x+dx)%width,(y+dy)%height)
            # print(new)
            if new2 not in walls and new not in visited:
                newqueue.append(new)
                if loop%2 == 1:
                    visited.add(new)
    # print(newqueue)


    queue = newqueue.copy()
print(len(visited))
draw()
