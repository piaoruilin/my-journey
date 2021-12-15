C = []
B = []
U = []
#day1, day2, day3, day4, day5, day6, day7
week1 = []
#chest, blood, urine
i = 1
count = 1

while i in range(8) :
    if i == 8 :
        count = count + 1
    print("DAY ", i, "of WEEK", count)
    data = int(input("Have you had chest pain today? : "))
    if data == 1 :
        C.append(1)
    else :
        C.append(0)

    data1 = int(input("Have you had blood pain today? : "))
    if data1 == 1:
        B.append(1)
    else :
        B.append(0)

    data2 = int(input("Have you had urine pain today? : "))
    if data2 == 1 :
        U.append(1)
    else :
        U.append(0)
    print ("")
    i += 1

sumc = sum(C)
sumb = sum(B)
sumu = sum(U)

week1.insert(0, sumc)
week1.insert(1, sumb)
week1.insert(2, sumu)

print(sum(C), "days of chest pain")
print(sum(B), "days of blood pain")
print(sum(U), "days of urine pain")
print("")

if sum(C) >= 4 :
    print("Irregular frequency of chest pain")
if sum(B) >= 2 :
    print("Irregular frequency of blood pain")
if sum(U) > 1 :
    print("Irregular frequency of urine pain")

cont = 7 - sumc
if cont >=4 :
    print("CONTINUOUS SYMPTOM")

print(week1)
