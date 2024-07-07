with open("./aoc/2023/06/data.txt") as f:
    data = [line.split("  ")[1:] for line in f.read().split("\n")]
print(data)
times,distances = [],[]
for num in data[0]:
    if num != "":
        times.append(int(num.strip()))
for num in data[1]:
    if num != "":
        distances.append(int(num.strip()))
print(times)
print(distances)


#distance = t(7 - t)
#t(7-t) > 9
#t^2 - 7t + 9 = 0

total = 1
for r in range(len(times)):
    ways = 0
    for speed in range(times[r]):
        distance = (times[r] - speed) * speed
        if distance > distances[r]:
            ways+=1
        elif ways > 0:
            break #no funny business
    total *= ways
            
print(total)