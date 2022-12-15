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

    if int(cpt1[1]) >= int(cpt1[2]) :
        if int(cpt1[3]) >= int(cpt1[0]) :    
            score +=1
            print("[",cpt1[0],"-",cpt1[1],"] , [",cpt1[2],"-",cpt1[3],"]"," le score est de : ",score)


print("\n//////////////////////////////////////")
print("PART 2 :")  
print("Le résultat 2 est : ",score)
print("//////////////////////////////////////\n\n")  

