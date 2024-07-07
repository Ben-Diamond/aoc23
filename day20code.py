with open("./aoc/2023/20/data.txt") as f:
    data = [x.replace("-> ","").replace(",","").split(" ") for x in f.read().split("\n")]
#print(data)

import math
#10894050654118238208 too high
#5447025327059119104
print(math.lcm(4051,4021,4057,3833))
#771404157191205888


exit()
thing = ['pc','hc','mf','rz','vl','lv',
 'jd','fr','mr','ml','pr','tb' ,
 'bh','bc','hd','fq','pk','qj',
'rq','nt','sq','kl','nh','kq',
     'cn','mb','ch','nf','jg','nd',
     'kk','fl','lj','cs','sm','bj']
for i in range(len(thing)):
    suspect = thing[i]

    links = {"rx":[]}
    # links = {"output":[]}
    flipflops = {}
    memories = {}
    for line in data:
        links[line[0][1:]] = line[1:]
        if line[0][0] == "%":
            flipflops[line[0][1:]] = 0
        elif line[0][0] == "&":
            memories[line[0][1:]] = {}
    #print(memories,"m")
    for l in links:
        for d in links[l]:
            if d in memories: #we are an input to the conjunction
                # if d not in memories:
                #     memories[d] = {}
                memories[d][l] = 0
    #print(flipflops)
    #print(memories)
    #print(links)
    # exit()
    def receivePulse(d,str,f):
        # if d in theSecondLayer:
        #     theSecondLayer[d] = str
        # newqueue.append((d,str))
        if d in memories:

            memories[d][f] = str
            # #print("receiving from",f,"strengtg",str,memories[d])
            if 0 in memories[d].values():
                str = 1
            else:
                str = 0
            #now send this pulse to everyone
            for out in links[d]:
                newqueue.append((out,str,d))
        elif d in flipflops:
            if str == 0:
                flipflops[d] = 1 - flipflops[d]
                for out in links[d]:
                    newqueue.append((out,flipflops[d],d))
        else: #a "roadcaster"
            for out in links[d]:
                newqueue.append((out,str,d))

    def erm():
    #&df -> rex
    #from four &s
    #these must all be 1
    #xl, ln, xp, gp pull from
    #zp, pp, sj, rg
    #so they invert these
    #so we want zp to emit 0?
    #everything that points to zp and pp and js and rg must be one
    #find loop for each "suspect" in the second layer
    #they are all flipflops (huh)
    #we want the loop of them turning on 
    #print(memories["zp"])
    # theSecondLayer = {}
    # for m in memories["df"]:
    #     # #print(memories[m])
    #     for mm in memories[m]:
    #         # #print(memories[mm])
    #         for mmm in memories[mm]:
    #             theSecondLayer[mmm] = [0,[]]
    #print(theSecondLayer)
    # exit()
    # suspect = "pc"
    # for suspect in theSecondLayer:
    #     if suspect in memories:
    #         #print("cond")
    #     else:
    #         #print("flop")
    # exit()
        
    #print(suspect)
    # exit()
    #IF NOT CONSIDERING STARTING POINT (probably wrong)  
    #4115,4067,6099,4179,4052,4053,5075,4307,4563,4022,6069,4149,5045,4025,4053,4533,4277,4037,
    #5081,4065,4121,4185,4569,4073,4058,4313,6105,3897,3849,3841,4345,3865,5881,3834,3961,4857,
    # import math
    # #print(math.lcm(4115,4067,6099,4179,4052,4053,5075,4307,4563,4022,6069,4149,5045,4025,4053,4533,4277,4037,5081,4065,4121,4185,4569,4073,4058,4313,6105,3897,3849,3841,4345,3865,5881,3834,3961,4857))
    # exit()
        pass
    
    onevalues = []
    differences = []
    for loop in range(1,int(10e8)):
        cur = flipflops[suspect]
        # #print("NEW LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOP")
        queue = [("roadcaster",0,None)] #TO - STRENGTH - FROM
        while queue != []:
            newqueue = []
            while queue != []: #lol
                dest,strength,fro = queue.pop(0)
                # #print(dest,strength,fro) #that means we RECEIVED this pulse
                # for dest in links[name]:
                receivePulse(dest,strength,fro)
            # #print("new queue",newqueue)
            # exit()
            queue = newqueue.copy()

        #find the pc loop  
        if cur == 0 and flipflops[suspect] == 1:
            onevalues.append(loop)
            if len(onevalues) > 1:
                new = loop - onevalues[-2]
                if new not in differences:
                
                    differences.append(new)    
                    #print("\n")
                # else:
                    #print(onevalues)
                    #print(differences)
                    #print(onevalues[-1])
                    # p=2
                    # p=onevalues[-1]
                    if i == 2 or i == 10 or i == 26 or i == 32:
                        print(differences)
                        break
                    if len(differences) == 2:
                       print(onevalues[-1]-onevalues[0])
                    #    print(differences,onevalues,i)
                       break                    

            # if len(differences) == 2 and loop % p==0:  
            #print(p)
            # exit()
            #print(onevalues)
                #4115 8230
                #even again at 8166
    # 211712400442661
    #~15 digits