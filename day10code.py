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
history = set()
history.add(start)
count = 0
print(connections)
while positions[0] != positions [1]:
# while True:
    history.add(positions[0])
    history.add(positions[1])
    # print(positions)

    positions[0] = connections[positions[0]][0] if connections[positions[0]][0] not in history else connections[positions[0]][1]
    positions[1] = connections[positions[1]][0] if connections[positions[1]][0] not in history else connections[positions[1]][1]
    
    count += 1
print(count) #add one to this lol

