with open("./aoc/2023/06/data.txt") as f:
    data = [line.replace(" ","").split(":")[1] for line in f.read().split("\n")]
print(data)



#distance = t(7 - t)
#t(7-t) > 9
#t^2 - 7t + 9 = 0
import math
#a = 1
b = int(data[0]) #TECHNICALLY minus but we wont do minus b
c = int(data[1])
print(b,c)
discriminant = b*b - 4*c
t1 = 0.5*(b + math.sqrt(discriminant))
t2 = 0.5*(b - math.sqrt(discriminant))
#as long as t1 and t2 are not integers it works
print(t1,t2)
print(math.floor(t1) - math.ceil(t2) + 1) #then round down