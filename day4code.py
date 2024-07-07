with open("./aoc/2023/04/data.txt") as f:
    data = [[x.replace("  "," ").split("|")[0].split(" ")[2:-1],x.replace("  "," ").split("|")[1].split(" ")[1:]] for x in f.read().split("\n")]
# print(data)

total = 0
for card in data:
    tempScore = 0
    for number in card[1]:
        if number in card[0]: #winning
            tempScore = 2*tempScore if tempScore > 0 else 1
    # print(tempScore)
    total+=tempScore
print(total)