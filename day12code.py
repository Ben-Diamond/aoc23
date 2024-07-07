




"""
iterate
prioritise "#"
if contradiction, reverse until find ? and swap it
because we prioritise 

# is 0
. is 1


start 0000
then evaluate
then increment:
    starting from the right,
    all . become #
    one # become .


"""

def increment(parts):
    # # is 0, . is 1, add 1 to this number but weird
    temp = ""
    flag = False
    for x in range(len(parts)-1,-1,-1): #looks funny, go backwards
        if flag == True:
            temp = parts[x] + temp
        elif parts[x] == ".":
            temp = "#" + temp
        else:
            temp = "." + temp
            flag = True
    return temp

def assemble(parts,mysteries):
    #take ?.?# and .# into ..##
    temp = ""
    c = 0
    for x in range(len(parts)):
        if parts[x] == "?":
            temp += mysteries[c]
            c += 1
        else:
            temp += parts[x]
    return temp

def check(parts,groupsNeeded):
    groupNumber = -1
    groupCount = 0
    for part in parts:
        
        # print(part)
        if part == "#":
            if groupCount == 0:
                groupNumber += 1
                if groupNumber >= len(groupsNeeded):
                    return False
            groupCount += 1
        elif part == ".":
            if groupCount > 0:
                # print(groupCount,groupNumber)
                if groupsNeeded[groupNumber] != groupCount: #oopsie
                    return False
                groupCount = 0
    # print("h")
    if parts[-1] == "#" and groupsNeeded[groupNumber] != groupCount or groupNumber != len(groupsNeeded) - 1: #oopsie
        # print("end",groupCount,groupNumber)
        return False
    # print(parts)
    return True

with open("./aoc/2023/12/data.txt") as f:
    data = [[x.split(" ")[0],[int(y) for y in x.split(" ")[1].split(",")]] for x in f.read().split("\n")]
# print(data)
total = 0
# data = [["?????????????#????", [1, 1, 10]]]
for line in data:

    parts = line[0]
    numberq = parts.count("?")
    groupsNeeded = line[1]
    mysteries = "#"*numberq
    while mysteries != "."*numberq:
        # print(assemble(parts,mysteries),"?")
        if check(assemble(parts,mysteries),groupsNeeded):
            total += 1
        mysteries = increment(mysteries)
    if check(assemble(parts,mysteries),groupsNeeded):
        total += 1
    print(total)
#7486 too low