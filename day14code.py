with open("./aoc/2023/14/data.txt") as f:
    data = [list(x) for x in f.read().split("\n")]

width,height = len(data[0]),len(data)

def draw(data):

    with open("./aoc/2023/14/map.txt","w") as f:
        out = ""
        for y in range(height):
            for x in range(width):
                out += data[y][x]
            out += "\n"
        f.write(out)
total = 0
for x in range(width):
    bottom = -1
    y = 0
    spheres = 0
    while y < height:
        if data[y][x] == "#":
            bottom,y = y,bottom
            #fill in O
            # print("h")
            while y < bottom:
                # print("why",y,"bottom",bottom,"x",x,"spheres",spheres)
                y += 1
                if spheres > 0:
                    data[y][x] = "O"
                    total += height - y
                    spheres -= 1
        elif data[y][x] == "O":
            data[y][x] = "."
            spheres += 1
        y+=1
    y = bottom
    while y < height:
        y += 1
        if spheres > 0:
            data[y][x] = "O"
            total += height - y
            spheres -= 1
    # print(data)

# draw(data)
print(total)