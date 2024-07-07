with open("./aoc/2023/19/data.txt") as f:
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
[(0,10e6),(0,10e6),(0,10e6),(0,10e6)]
then [(0,10e6),(0,10e6),(0,10e6),(0,1031)] moves to the next layer
and [(0,10e6),(0,10e6),(0,10e6),(1031,10e6)] moves to the next item
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
                thing = (0,temp-1)
            else:
                thing = (temp+1,10e6)
            links[fro].append([to,letters[bit[0][0]],thing])
            
        # links[fro][to] = thing
print(links)
"""
and the traversal begins!

(0,10e6)
"""
# places = {
    # "in":[(0,10e6),(0,10e6),(0,10e6),(0,10e6)]
# }
total = 0
for line in data[1]:
    line = line[1:-1]
    values = [int(x[2:]) for x in line.split(",")]
    place = "in"
    while True:
        print("place",place)
        if place == "A":
            print("win",values)
            total += sum(values)
            break
        elif place == "R":
            print("lose",values)
            break
        #ok let's go
        for link in links[place]:
            #link is [to,letter, (0,10e6)]

            if len(link) == 1:#go there
                place = link[0]
                break
            else:
                to,letter,span = link              
                if values[letter] >= span[0] and values[letter] <= span[1]: #inside
                    place = to
                    break

        # exit()
print(total)
#446230 too low