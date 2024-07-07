with open("./aoc/2023/15/data.txt") as f:
    data = [x.split("=") if "=" in x else [x[:-1]] for x in f.read().split(",")]
print(data)
boxes = [{} for x in range(256)]
for instruction in data:
    value = 0
    for letter in instruction[0]:
        value += ord(letter)
        value = (17*value)%256
    #value is box index
    if len(instruction) == 1: #remove
        # for n in range(len(data[value])):
            # if data[value][n] == instruction[0]
                # data[value].remove(instruction[0])
        boxes[value].pop(instruction[0],None)
    else:
        if instruction[0] not in boxes[value]:
            boxes[value][instruction[0]] = 0
        boxes[value][instruction[0]] = instruction[1]
print(boxes)

total = 0
for b in range(len(boxes)):
    box = boxes[b]
    x = 0
    for lens in box:
        x+=1
        total += (b+1)*x*(int(box[lens]))
print(total)