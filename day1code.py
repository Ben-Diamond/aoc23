with open("./aoc/2023/01/data.txt") as f:
    data = f.read().split("\n")
print(data)
total = 0
for line in data:
    first, last = "",""
    for l in line:
        if l.isdigit():
            if first == "":
                first = l
            last = l
    total+=int(first + last)
    # print(first,last)S
print(total)
