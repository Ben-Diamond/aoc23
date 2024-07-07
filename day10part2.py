with open("./aoc/2023/10/data.txt") as f:
    data = f.read().split("\n")

connections = {}

for y in range(len(data)):
    for x in range(len(data[0])):
        pipe = data[y][x]
        match pipe:                
            case "-": #left, right
                connections[(y,x)] = [(y,x-1),(y,x+1)]
            case "|": #above, below
                connections[(y,x)] = [(y-1,x),(y+1,x)]
            case "L": #above, right
                connections[(y,x)] = [(y-1,x),(y,x+1)]
            case "J": #above, left
                connections[(y,x)] = [(y-1,x),(y,x-1)]
            case "7": #below, left
                connections[(y,x)] = [(y+1,x),(y,x-1)]
            case "F": #below, right 
                connections[(y,x)] = [(y+1,x),(y,x+1)]
            case "L": #above, right
                connections[(y,x)] = [(y-1,x),(y,x+1)]
            case "S": #start!!!
                start = (y,x)
            # case ".":
            #     bigBlankTiles.add((y,x))
# print(start)
positions = []
if (start[0]-1,start[1]) in connections and start in connections[(start[0]-1,start[1])]: #points to start
    positions.append((start[0]-1,start[1]))
if (start[0]+1,start[1]) in connections and start in connections[(start[0]+1,start[1])]: #points to start
    positions.append((start[0]+1,start[1]))
if (start[0],start[1]+1) in connections and start in connections[(start[0],start[1]+1)]: #points to start
    positions.append((start[0],start[1]+1))
if (start[0],start[1]-1) in connections and start in connections[(start[0],start[1]-1)]: #points to start
    positions.append((start[0],start[1]-1))
connections[start] = positions #new
history = set()
history.add(start)
count = 0
# print(connections)

while positions[0] != positions [1]:
    history.add(positions[0])
    history.add(positions[1])
    positions[0] = connections[positions[0]][0] if connections[positions[0]][0] not in history else connections[positions[0]][1]
    positions[1] = connections[positions[1]][0] if connections[positions[1]][0] not in history else connections[positions[1]][1]
history.add(positions[0])
history.add(positions[1])
""""
double the width and height, turning every pipe into a wall and adding walls between pipes that connect, adding spaces where they do not
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
becomes
. . . . . . . . .
.000000000000000.
 0             0 
.0 00000000000 0.
 0 0         0 0 
.0 0 . . . . 0 0.
 0 0         0 0 
.0 0 . . . . 0 0.
 0 0         0 0 
.0 00000 00000 0.
 0     0 0     0 
.0 . . 0 0 . . 0.
 0     0 0     0 
.0000000 0000000.
. . . . . . . . .

then use some kind of search algorithm to start at a point, find a way out and pick up other tiles that can escape along the way
if we run out of spaces to explore then cant escape and add to total
"""

walls = set()
for wall in history:
    #SPECIAL CASE FOR START?
    x,y = wall
    walls.add((2*x,2*y))
    walls.add((x + connections[wall][0][0], y + connections[wall][0][1])) #in the middle of this and what it points to
    walls.add((x + connections[wall][1][0], y + connections[wall][1][1]))
#escape from example 3 with normal map
# print(walls)
width = 2*len(data[0]) - 1
height = 2*len(data) - 1
def draw():
    f = open("./aoc/2023/10/map.txt","w")
    out = ""
    for y in range(height):
        for x in range(width):
            if (y,x) in walls:
                out += "0"
            elif y%2 == 0 and x%2 == 0:
                out += "."
            else:
                out += " "
        out += "\n"
    f.write(out)
    f.close()
    #actually helpful diagram

draw()
escapists = set()
def escape(y,x): #if in escapists skip
    #attempt to escape
    explored = set()
    # potentialEscapists = [(y,x)]
    potentialEscapists =  set()
    potentialEscapists.add((y,x))
    explored.add((y,x))
    newStuff = True
    escaped = False
    while newStuff:
        newStuff = False
        # print("e",explored)
        temp = set()
        for i in explored:
            y,x = i
            
            if y == 0 or y == height - 1 or x == 0 or x == width - 1:
                #we have escaped
                escaped = True
            #look above
            if (y+1,x) not in walls and (y+1,x) not in explored and y < height - 1:
                temp.add((y+1,x))
                newStuff = True
                if (y+1) % 2 == 0 and x % 2 == 0:
                    #this tile was on the original map and not in the main loop
                    potentialEscapists.add((y+1,x))

            if (y-1,x) not in walls and (y-1,x) not in explored and y > 0:
                temp.add((y-1,x))
                newStuff = True
                if (y-1) % 2 == 0 and x % 2 == 0:
                    potentialEscapists.add((y-1,x))

            if (y,x+1) not in walls and (y,x+1) not in explored and x < width - 1:
                temp.add((y,x+1))
                newStuff = True
                if y % 2 == 0 and (x+1) % 2 == 0:
                    potentialEscapists.add((y,x+1))

            if (y,x-1) not in walls and (y,x-1) not in explored and x > 0:
                temp.add((y,x-1))
                newStuff = True
                if y % 2 == 0 and (x-1) % 2 == 0:
                    potentialEscapists.add((y,x-1))
                
            #what if we are on the edge?
        explored = explored.union(explored,temp)
    if escaped:
        # print("p",potentialEscapists)
        # print(len(potentialEscapists))

        return [potentialEscapists,True]
    # print(width//2*height//2 - len(potentialEscapists))
    # print(len(history))
    # print("sad!")
    return [potentialEscapists,False]
failures = set()
for y in range(0,height,2):
    for x in range(0,width,2):
        if (y,x) not in walls and (y,x) not in escapists and (y,x) not in failures:
            temp = escape(y,x)
            if temp[1] == False: #sad!
                failures = failures.union(failures,temp[0])
                # print(temp[0])
            else:
                escapists = escapists.union(escapists,temp[0])
    print(y)
print(len(escapists))
print(failures)
print(len(failures))