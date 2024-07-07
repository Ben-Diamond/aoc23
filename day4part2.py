with open("./aoc/2023/04/data.txt") as f:
    data = [[x.replace("  "," ").split("|")[0].split(" ")[2:-1],x.replace("  "," ").split("|")[1].split(" ")[1:], 1] for x in f.read().split("\n")]
# print(data)

total = 0
for c in range(len(data)):
    tempScore = 0
    total += data[c][2]
    for number in data[c][1]:
        if number in data[c][0]: #win more cards!!!
            tempScore += 1
            data[c + tempScore] [2] += data[c][2] 
            #the card we win is in the location c + score, we win equal to number of copies of this card



print(total)