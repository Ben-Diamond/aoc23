[data := open("./aoc/2023/11/data.txt").read().split("\n"),galaxies:=[],emptyY := {y: True if False not in [True if data[y][x] == "." else False for x in range(len(data[0]))] else False for y in range(len(data))},emptyX := {x: True if False not in [True if data[y][x] == "." else False for y in range(len(data))] else False for x in range(len(data))}, expansions:=lambda v1,v2,empties,scale:scale*sum([1 if empties[x] == True else 0 for x in range(min(v1,v2),max(v1,v2))]),y:=0,galaxies:= set([(x,y) if data[y][x] == "#" else (-1,-1) for x in range(len(data[y]))for y in range(len(data))]),print(sum([sum([abs(x2 - x1) + abs(y2 - y1) + expansions(x1,x2,emptyX,1000000-1) + expansions(y1,y2,emptyY,1000000-1) if x1 != -1 and x2 != -1 and (x2 > x1 or (x2 == x1 and y2 > y1)) else 0 for x2, y2 in galaxies]) for x1,y1 in galaxies]))]