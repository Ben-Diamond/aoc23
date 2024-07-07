with open("./aoc/2023/05/data.txt") as f:
    data = f.read().split("\n\n")
print(data)
data2 = []
seeds = [int(x) for x in data[0].split(" ")[1:]]
seeds2 = []
for x in range(len(seeds)//2):
    seeds2.append([seeds[2*x],seeds[2*x + 1]])
print(seeds2)
data = data[1:]
print(data)
print(seeds)
for line in data:
    ranges = [x.split(" ") for x in line.split("\n")[1:]]
    for x in range(len(ranges)):
        ranges[x] = [int(ranges[x][0]),int(ranges[x][1]),int(ranges[x][2])]
    data2 = [ranges] + data2

#a line = list of ranges
#a range = output start, input start, count

def overlap(l1,u1,l2,u2):
    lower,upper = False,False
    #four cases
    #1 : 1 starts inside 2
    if l1 >= l2 and l1 <= u2:
        lower = l1
        if u2 > u1: 
            upper = u1
        else: #2 : fully contained 
            upper = u2

    elif l2 >= l1 and l2 <= u1:
        lower = l2
        if u2 > u1:
            upper = u1
        else:
            upper = u2
    return lower,upper

#work backwards, try seed
seed = 99700000
while True:
    # location = [seed,seed]
    location = seed
    for service in data2:
        for rrange in service: 
            #how can we get here?
            if rrange[0] <= location and rrange[0] + rrange[2] > location:
                location = rrange[1] + location - rrange[0]
                break #?
            #else no change...
        # print(location)
    for s in range(len(seeds)//2):
        if location >= seeds[2*s] and location < seeds[2*s] + seeds[2*s+1]:
            print(location,seed)
            exit()
    seed+=1 #increase this to home in on value