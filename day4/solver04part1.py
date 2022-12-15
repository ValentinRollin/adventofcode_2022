import re

file = open("input_04.txt")
data=[]
limit = ' '


for line in file.readlines(): 
    element = []
    for token in line.strip().split(limit):
        data.append(token)


score = 0

for a in data :
    cpt1 = re.split('[-, .]+', a)
   # print("test separateur",cpt1)

    #case 4-17,4-9
    if int(cpt1[0]) == int(cpt1[2]) :
        score += 1
        print(cpt1[0], " == ", cpt1[2], ": [",cpt1[0],"-",cpt1[1],"]","contient ","[",cpt1[2],"-",cpt1[3],"]"," le score est de : ",score)

    #case 3-10,5-10 + pas de doublon si 3-4,3-4
    if int(cpt1[1]) == int(cpt1[3]) and int(cpt1[0]) != int(cpt1[2]):
        score += 1
        print(cpt1[1]," == ",cpt1[3],": [",cpt1[2],"-",cpt1[3],"]","contient ","[",cpt1[0],"-",cpt1[1],"]"," le score est de : ",score)

    # case 5-7,3-9
    if int(cpt1[0]) > int(cpt1[2]) : 
        if int(cpt1[1]) < int(cpt1[3]) :
            score+=1
            print(cpt1[0]," > ",cpt1[2], ": [",cpt1[2],"-",cpt1[3],"]","contient ","[",cpt1[0],"-",cpt1[1],"]"," le score est de : ",score)
    
    # case 4-9,6-8
    if int(cpt1[0]) < int(cpt1[2]): 
        if int(cpt1[1]) > int(cpt1[3]):
            score+=1
            print(cpt1[0]," < ",cpt1[2], ": [",cpt1[0],"-",cpt1[1],"]","contient ","[",cpt1[2],"-",cpt1[3],"]"," le score est de : ",score)




print("\n//////////////////////////////////////")
print("PART 1 :")      
print("Le résultat est : ", score)
print("//////////////////////////////////////\n\n")  

