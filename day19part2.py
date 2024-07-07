with open("./aoc/2023/19/example.txt") as f:
    data = [x.split("\n") for x in f.read().split("\n\n")]
# print(data)
get = {}

def overlap(t1,t2):
    if t1[0] > t2[1] or t2[0] > t1[1]:
        return ((-1,-1))
    return (max(t1[0],t2[0]),min(t1[1],t2[1]))
def outside(t1,t2): #we want t1 without t2
    if t1[0] >= t2[0] and t1[1] <= t2[1]:
        return ((-1,-1))
    if t1[0] < t2[0]:
        if t1[1] > t2[1]: #both sides
            return ((t1[0],t2[0]-1),(t2[1]+1,t1[1]))
        return ((t1[0],t2[0]-1))
    if t1[1] > t2[1]:
        return ((t2[1]+1,t1[1]))
    print("???")
    exit()

"""
REBOOT
after compiling dictionary...
start at in
split into cases for variables
[xmas]
[(0,4000),(0,4000),(0,4000),(0,4000)]
then [(0,4000),(0,4000),(0,4000),(0,1031)] moves to the next layer
and [(0,4000),(0,4000),(0,4000),(1031,4000)] moves to the next item
should all be single ranges????

such that links[fro][letter]

"""

#get awesome dictionary
links = {}
letters = {"x":0,"m":1,"a":2,"s":3}
#such that

for line in data[0]:
    fro = line.split("{")[0]
    line = line.split("{")[1].replace("}","").split(",")
    links[fro] = []
    # print(line)
    for bit in line:
        bit = bit.split(":")
        if len(bit) == 1:
            to = bit[0]
            thing = {}
            links[fro].append([to])
            #the end
           
        else:
            to = bit[1]
            temp = int(bit[0][2:])
            if "<" in bit[0]:
                thing = (1,temp-1)
            else:
                thing = (temp+1,4000)
            links[fro].append([to,letters[bit[0][0]],thing])
            
        # links[fro][to] = thing
print(links)
exit()
"""
and the traversal begins!

(0,4000)
"""
# places = {
    # "in":[(0,4000),(0,4000),(0,4000),(0,4000)]
# }
total = 0
a=0
paths = [["in",(1,4000),(1,4000),(1,4000),(1,4000)]]
while paths != []: #idk
    newpaths = []
    for path in paths:
        print("path",path)
        if path[0] == "R":
            continue
        if path[0] == "A":
            total += (path[1][1]-path[1][0]+1)*(path[2][1]-path[2][0]+1)*(path[3][1]-path[3][0]+1)*(path[4][1]-path[4][0]+1)
            continue
        #SPLIT it up
        places = links[path[0]]
        print("places",places)
        for place in places:
            if len(place) == 1:
                path[0] = place[0]
                newpaths.append(path) #probably
            else:
                letter = place[1]+1
                nextpath = path.copy()
                nextpath[letter] = overlap(path[letter],place[2])
                nextpath[0] = place[0]
                newpaths.append(nextpath)
                path[letter] = outside(path[letter],place[2]) #continue with this
                path[0] = place[0]

    paths = newpaths.copy()
    # print(paths)
    # if a == 1:
    #     exit()
    # a=2
print(total)