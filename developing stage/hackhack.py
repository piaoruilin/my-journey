chest = []
head = []
week1 = [chest, head]
month = [week1, week2, week3, week4]
i=1
n=0
m=4

while i<1000 :
    if i>m :
        m=m+1
    print("WEEK ", i, "of MONTH", n)
    
    chest = int(input("Chest Pain : "))
    if chest == 1 :
        chest.append(1)
    else :
        chest.append(0)

    head = int(input("Head Pain : "))
    if head == 1 :
        head.append(1)
    else :
        head.append(0)
    i += 1

print(week1)
