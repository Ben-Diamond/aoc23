with open("./aoc/2023/03/data.txt") as f:
    data = f.read().split("\n")
print(data)
width = len(data[0])
height = len(data)

def check(x,y):
    #true if a symbol
    symbol = data[y][x]
    if symbol.isdigit() or symbol == ".":
        return False
    return True
f = open("./aoc/2023/03/info.txt","w")
total = 0
number = ""
adj = False
for y in range(height):
    for x in range(width):
        if data[y][x].isdigit():
            #check diagonal left only on the first one
            if number == "":
                adj = False
                if y>=1 and x>=1 and check(x-1,y-1): #up left
                    adj = True
                if y+1<height and x>=1 and check(x-1,y+1): #down left
                    adj = True

            number+=data[y][x]
            if not adj:
                if y>=1 and check(x,y-1):#check above
                    adj = True
                if y+1<height and check(x,y+1):#check below
                    adj = True
                if x>=1 and check(x-1,y):#check left
                    adj = True
                if x+1<width and check(x+1,y):#check right
                    adj = True
                if y>=1 and x+1<width and check(x+1,y-1): #up right
                    adj = True
                if y+1<height and x+1<height and check(x+1,y+1): #down right
                    adj = True
        else:
            if number!= "":            
                if adj == True:
                    f.write(f"{number}\n")
                    total += int(number)
                else:
                    f.write(f"{number} bad\n")
                number = ""

print(total)
f.close()