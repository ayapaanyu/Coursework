### Aya Ishida (MSc IT) 
### ISD Term2 Coursework 1, Submitted at 9/2/2016
### Question 2

def ValidJunctions(lines):
    ## Split words by "," and store them in the list called "line".
    i = 0
    line = []
    for lines[i] in lines:
        item=lines[i].rstrip("\n")
        line.append(item)
        i=i+1
        
    ## Junction check
    junStart = 2
    junEnd = line.index('Junctions END')
    junDic = {}
    ### Store Junction data in the dictionary called junDic with the key of junction name.
    ### Check if the key has already been in the dictionary.
    ### If so, return duplicated error.
    while junStart < junEnd:
        junData = line[junStart].split(",")
        if junData[0] in junDic:
            raise LookupError ("A Junction has been defined twice")
        else:
            junDic[junData[0]]=int(junData[1]),int(junData[2])
        junStart = junStart+1
             
    ## Association check
    AssoStart = junEnd+2
    AssoEnd = len(line)-1
    ### Check if there is the same junction name in the dictionary.
    ### If not, return undefined error.
    while AssoStart < AssoEnd:
        AssoData = line[AssoStart].split(",")
        if AssoData[0] not in junDic:
            raise LookupError("There is an undefined junction")
        elif AssoData[1] not in junDic:
            raise LookupError("There is an undefined junction")
        AssoStart = AssoStart+1


try:
    inf = open("network1.txt", "r")
    lines = inf.readlines()
    ValidJunctions(lines)
    print("Successful")
except LookupError as except0bj:
    print("Error:",str(except0bj))

try:
    inf = open("network2.txt", "r")
    lines = inf.readlines()
    ValidJunctions(lines)
    print("Successful")
except LookupError as except0bj:
    print("Error:",str(except0bj))

try:
    inf = open("network3.txt", "r")
    lines = inf.readlines()
    ValidJunctions(lines)
    print("Successful")
except LookupError as except0bj:
    print("Error:",str(except0bj))

try:
    inf = open("network4.txt", "r")
    lines = inf.readlines()
    ValidJunctions(lines)
    print("Successful")
except LookupError as except0bj:
    print("Error:",str(except0bj))
    
try:
    inf = open("networkFail1.txt", "r")
    lines = inf.readlines()
    ValidJunctions(lines)
    print("Successful")
except LookupError as except0bj:
    print("Error:",str(except0bj))

try:
    inf = open("networkFail2.txt", "r")
    lines = inf.readlines()
    ValidJunctions(lines)
    print("Successful")
except LookupError as except0bj:
    print("Error:",str(except0bj))
