with open("./aoc/2023/08/data.txt") as f:
    moves,nodes = [x.split("\n") if "\n" in x else x for x in f.read().split("\n\n")]
print(moves)
positions = []
times = []
# zeds = set()
maps = {}
for line in nodes:
    maps[line.split(" = ")[0]] = {"L":line.split("(")[1][:3], "R":line.split(", ")[1][:3]}
    # if line[-2] == "Z":
    #     print("zed",line)
    #     zeds.add(line.split(", ")[1][:3])
    if line[2] == "A":
        print("ay",line)
        times.append(0)
        positions.append(line.split(" = ")[0])
# exit()
print(positions)
for p in range(len(positions)):
    check = False
    while not check:
        for instruction in moves:
            times[p] += 1
            newPos = maps[positions[p]][instruction]
            # print(newPos)
            positions[p] = newPos
            if newPos[2] == "Z":
                check = True
                break
print(times)
total = 1
#all multiples of 277 (?)
import math
for a in times:
    print(math.gcd(a,total))
    total = a*total // math.gcd(a, total)
print(total)
    #     allZ = True
    #     steps += 1
    #     for p in range(len(positions)):
    #         newPos = maps[positions[p]][instruction]
    #         if newPos[2] != "Z":
    #             allZ = False
    #         positions[p] = newPos
    #     if allZ:
    #         print(steps,positions)
    #         exit()
    # print(positions)