with open("./aoc/2023/21/data.txt") as f:
    data = f.read().split("\n")
print(data)
width = len(data[0])
height = len(data)
walls = set()
for y in range(height):
    for x in range(width):
        if data[y][x] == "#":
            walls.add((x,y))
        elif data[y][x] == "S":
            start = (x,y)

def draw():
    out = ""
    for y in range(height):
        for x in range(width):
            if (x,y) in walls:
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


queue = [start]
for loop in range(64):
    newqueue = []
    for x,y in queue:
        #attempt to move twice
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            new = (x+dx,y+dy)
            if new not in walls and new not in visited:
                newqueue.append(new)
                if loop%2 == 1:
                    visited.add(new)
    print(newqueue)


    queue = newqueue.copy()
print(len(visited))
draw()