with open("./aoc/2023/02/data.txt") as f:
    data = f.read().split("\n")

data = [line.split(";") for line in data]
max = {"red":12,"green":13,"blue":14}
# print(data)
total = 0
for l,line in enumerate(data):
    work = True
    for game in line:
        game = game.split()
        # print(game)
        for w in range(len(game)):
            word = game[w].replace(",","").replace(";","")
            if word in max and int(game[w-1]) > max[word]:
                # print("uh oh",l,word,game[w-1])
                work = False
    if work:
        total+=l+1
print(total)