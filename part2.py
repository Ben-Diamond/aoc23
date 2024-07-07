with open("./aoc/2023/01/data.txt") as f:
    data = f.read().split("\n")
print(data)
total = 0
numbers = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9",
            "1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}

for line in data:
    first,last,currentWord = "","",""
    for l in range(len(line)):
        for word in numbers:
            if line[l:l+len(word)] == word:
                if first == "":
                    first = numbers[word]
                last = numbers[word]
    total += int(first+last)
    # print(first,last)
print(total)