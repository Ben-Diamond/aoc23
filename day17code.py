with open("./aoc/2023/17/data.txt") as f:
    data = f.read().split("\n")
print(data)


width, height = len(data[0]),len(data)
def draw(data,result):
    out = "\n"
    for y in range(height):
        for x in range(width):
            if (x,y) in result:
                out += "#"
            else:
                out += "."
                # out += data[y][x]
        out += "\n"
    
    with open("./aoc/2023/17/drawing.txt","a") as f:
        f.write(out)
pass

def dequeue(q): #queue = queue.pop(dequeue(queue))
    # lowest = 10000
    # for p in range(len(q)):
    #     if q[p][5] < lowest:
    #         lowest = q[p][5]
    #         o = p
    # return o
    return 0

def enqueue(q,state): #insert
    if q == []:
        return [state]
    p=0
    while q[p][5] < state[5]:
        p+=1
        if p == len(q):
            break
    q.insert(p,state)
    # print("q",q)
    return q

# visited = {}
visited = set()
queue = [(0,0,0,0,0,0)]
#that's x,y,dx,dy,n,d
#n=number of times we have moved in that direction
c=0
while queue != []:
    # print(queue)
    c+=1
    x,y,dx,dy,n,d = queue.pop(dequeue(queue))
    if c%1000 == 0:
        print(c,x,y,dx,dy,n,d,len(queue))
    # x,y,dx,dy,n,d = state.values()
    #start with dx,dy = CURRENT facing direction
    if x == width-1 and y == height-1:
        print(d) #SUBTRACT THE FIRST NUMBER
        exit()
    if x==-1 or x==width or y==-1 or y==height:
        continue
    if (x,y,dx,dy,n) in visited:
        continue
    visited.add((x,y,dx,dy,n))

    for dx1,dy1 in [(1,0),(-1,0),(0,1),(0,-1)]: 
        if (dx1,dy1) == (-1*dx,-1*dy):
            continue
        if x+dx==-1 or x+dx==width or y+dy==-1 or y+dy==height:
                continue
        if (dx1,dy1) == (dx,dy):
            if n == 3: #too long
                continue
            queue = enqueue(queue,(x+dx,y+dy,dx1,dy1,n+1,d+int(data[y+dy][x+dx])))
        else:
            queue = enqueue(queue,(x+dx,y+dy,dx1,dy1,1,d+int(data[y+dy][x+dx])))
print(queue)

