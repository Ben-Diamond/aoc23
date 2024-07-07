with open("./aoc/2023/03/data.txt") as f:
    data = f.read().split("\n")
print(data)
width = len(data[0])
height = len(data)

ancientGears = {}
for y in range(height):
    for x in range(width):
        if data[y][x] == "*":
            ancientGears[(y,x)] = {"num":0,"sum":0}


# def check(x,y):
    # #true if a symbol
    # if y>0:#up
    #     if x>0 and data[y-1][x-1] == "*": #up left
    #         return True
    #     if data[y-1][x] == "*": #up
    #         return True
    #     if x+1<width and data[y-1][x+1] == "*": #up right
    #         return True
    # if x>0 and data[y][x-1] == "*": #left
    #     return True
    # if x+1<width and data[y][x+1] == "*": #right
    #     return True
    # if y+1<height:#down
    #     if x>0 and data[y+1][x-1] == "*": #down left
    #         return True
    #     if data[y+1][x] == "*": #down
    #         return True
    #     if x+1<width and data[y+1][x+1] == "*": #down right
    #         return True
    # return False

total = 0
number = ""
adj = False
adjGears = {}
for y in range(height):
    for x in range(width):
        if data[y][x].isdigit():
            number+=data[y][x]

            if not adj:
                for y1 in [-1,0,1]:
                    for x1 in [-1,0,1]:
                        if (y+y1,x+x1) in ancientGears:
                            adj = True
                            # if (y+y1,x+x1) not in ad
                            # adjGears.append((y+y1,x+x1))
                            adjGears[(y+y1,x+x1)] = "huh"
                            # print(y+y1,x+x1)
                            # print(adjGears)


        else:
            if number!= "":            
                if adj == True:
                    for g in adjGears:
                        if ancientGears[g]["num"] == 0:

                            ancientGears[g]["num"] = 1
                            ancientGears[g]["sum"] = int(number)
                        elif ancientGears[g]["num"] == 1:
                            ancientGears[g]["num"] = 2
                            ancientGears[g]["sum"] *= int(number)
                        else:
                            ancientGears[g]["num"] = 3
            adjGears = {}
            number = ""
            adj = False

print(ancientGears)
for g in ancientGears:
    if ancientGears[g]["num"] == 2:
        total += ancientGears[g]["sum"]
print(total)