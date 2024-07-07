with open("./aoc/2023/16/data.txt") as f:
    data = f.read().split("\n")
#print(data)
width,height = len(data[0]),len(data)


#print(result)
total = 0
for x0 in range(width):
    for y0 in range(height):
        if x0 > 0 and x0 < width - 1:
            if y0 > 0 and y0 < height - 1:
                continue #very lazed
        # print(x0,y0)
        for p in [(1,0),(-1,0),(0,1),(0,-1)]:
            dx, dy = p
            # if data[y0][x0] == "\\": #swap
            #     dy, dx = dx, dy
            paths = [(x0 - dx,y0 - dy,dx,dy)]
            result = set()
            states = set()
            while len(paths) > 0:
                newpaths = []
                for path in paths:
                    # print(path)
                    if path in states:
                        # print("already")
                        continue
                    x,y,dx,dy = path
                    states.add(path)
                    result.add((x,y))
                    if x + dx == width or x + dx == -1 or y + dy == height or y + dy == -1:
                    #end
                        continue
                    new = data[y+dy][x+dx]
                    if new == ".":
                        #yeah
                        newpaths.append((x+dx,y+dy,dx,dy))

                    elif new == "|":
                        if dy == 0:
                            #split
                            newpaths.append((x+dx,y+dy,0,1))
                            newpaths.append((x+dx,y+dy,0,-1))
                        else:
                            newpaths.append((x+dx,y+dy,dx,dy))
                        
                    elif new == "-":
                        if dx == 0:
                            #split
                            newpaths.append((x+dx,y+dy,1,0))
                            newpaths.append((x+dx,y+dy,-1,0))
                        else:
                            newpaths.append((x+dx,y+dy,dx,dy))
                        #split
                    elif new == "\\":
                        newpaths.append((x+dx,y+dy,dy,dx))
                        pass
                    elif new == "/":
                        newpaths.append((x+dx,y+dy,-1*dy,-1*dx))
                paths = newpaths.copy()
            if len(result) - 1 > total:
                total = len(result) - 1
                print(total)
# def draw(result,data):
#     out = ""
#     for y in range(height):
#         for x in range(width):
#             if (x,y) in result:
#                 out += "#"
#             else:
#                 out += data[y][x]
#         out += "\n"
#     with open("./aoc/2023/16/drawing.txt","w") as f:
#         f.write(out)
# draw(result,data)
#7743 too high
                
print("a",end="")
print("a",end="\nbigchungus")