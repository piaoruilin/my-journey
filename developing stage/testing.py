chest = []
joint = []
head = []
array = []
i = 0

while i in range (0, 7) :
    sym = input("Your symptom today : ")

    if sym == "chest" :
        chest.append(1)
    elif sym != "chest" :
        chest.append(0)
    elif sym == "joint" :
        joint.append(1)
    elif sym != "joint" :
        joint.append(0)
    elif sym == "head" :
        head.append(1)
    elif sym != "head" :
        head.append(0)
    else :
        sym = input("Your symptom today : ")
    i += 1

array.insert(0, chest)
array.insert(1, joint)
array.insert(2, head)
        
print(array)
        
        
