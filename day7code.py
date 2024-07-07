with open("./aoc/2023/07/data.txt") as f:
    data = [{ "hand":line.split(" ")[0], "points":int(line.split(" ")[1]), "rank":0, "type":None }for line in f.read().split("\n")]
orderCards = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}
orderHands = {"five":7,"four":6,"house":5,"three":4,"two pairs":3,"pair":2,"bad":1}


def better(c1,c2):
    if c1["type"] > c2["type"]:
        return True
    if c2["type"] > c1["type"]:
        return False
    for p in range(5):
        if orderCards[c1["hand"][p]] > orderCards[c2["hand"][p]]:
            return True
        if orderCards[c1["hand"][p]] < orderCards[c2["hand"][p]]:
            return False
    print("???")


for x in range(len(data)):
    hand = data[x]["hand"]
    counts = {}
    for l in range(len(hand)):
        if hand[l] not in counts:
            counts[hand[l]] = 0
        counts[hand[l]] += 1
    counts = sorted([counts[c] for c in counts],reverse=True)
    # print(counts)
    if counts == [5]: #5
        data[x]["type"] = 7
    elif counts == [4,1]: #4
        data[x]["type"] = 6
    elif counts == [3,2]: #house
        data[x]["type"] = 5
    elif counts == [3,1,1]: #three
        data[x]["type"] = 4
    elif counts == [2,2,1]: #two pairs
        data[x]["type"] = 3
    elif counts == [2,1,1,1]: #pair
        data[x]["type"] = 2
    elif counts == [1,1,1,1,1]: #bad
        data[x]["type"] = 1 
    else:
        print("???")

    # print("type",data[x]["type"])
    #find out everything better than it and increment its rank by 1
    #only look at things before x
    rank = 1
    for c in range(x):
        if better(data[x],data[c]):
            rank +=1
        else:
            data[c]["rank"] += 1
    data[x]["rank"] = rank
    # print(data[x])

total = 0
for hand in data:
    total += hand["rank"] * hand["points"]
print(data)
print(total)