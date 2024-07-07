with open("./aoc/2023/09/example2.txt") as f:
    data = f.read().split("\n")
for l in range(len(data)):
    data[l] = [int(x) for x in data[l].split(" ")]
print(data)
def allZeroes(nums):
    for n in range(len(nums)):
        if nums[n] != 0:
            return False
    return True
total = 0
for seq in data:
    differences = [seq]
    lastDiff = [seq]
    while not allZeroes(lastDiff):
        lastDiff = differences[-1]
        differences.append([lastDiff[x+1] - lastDiff[x] for x in range(len(lastDiff) - 1)])
        # print(differences)
        total += lastDiff[-1]
print(total)