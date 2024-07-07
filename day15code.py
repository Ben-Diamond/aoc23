with open("./aoc/2023/15/data.txt") as f:
    data = f.read().split(",")
print(data)
total = 0
for word in data:
    value = 0
    for l in range(len(word)):
        value += ord(word[l])
        value *= 17
        value = value % 256
        print(value)
    total += value
    # print(value)
print(total)