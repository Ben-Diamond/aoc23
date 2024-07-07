with open("./aoc/2023/05/data.txt") as f:
    data = f.read().split("\n\n")
print(data)
data2 = []
seeds = [int(x) for x in data[0].split(" ")[1:]]
data = data[1:]
print(data)
print(seeds)
for line in data:
    ranges = [x.split(" ") for x in line.split("\n")[1:]]
    for x in range(len(ranges)):
        ranges[x] = [int(ranges[x][1]),int(ranges[x][0]),int(ranges[x][2])]
    data2.append(ranges)

#a line = list of ranges
#a range = input start, output start, count
print(data2)
lowest = 10e20
for seed in seeds:
    location = seed
    for service in data2:
        for rrange in service:
            # print(rrange)

            if rrange[0] <= location and rrange[0] + rrange[2] > location:
                location = rrange[1] + location - rrange[0]
                break
    if location < lowest:
        lowest = location
        print(location)
