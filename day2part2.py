with open("./aoc/2023/02/data.txt") as f:
    data = f.read().split("\n")

data = [line.split(";") for line in data]

# print(data)
total = 0
for l,line in enumerate(data):
    minimum = {"red":0,"blue":0,"green":0}

    for game in line:
        game = game.split()
        # print(game)
        for w in range(len(game)):
            word = game[w].replace(",","").replace(";","")
            if word in minimum and int(game[w-1]) > minimum[word]:
                minimum[word] = int(game[w-1])
                # print("uh oh",l,word,game[w-1])
    # print(minimum)
    total+=minimum["red"]*minimum["blue"]*minimum["green"]




print(total)