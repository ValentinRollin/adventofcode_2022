import re

file = open("input_06.txt")
data=[]

for line in file.readlines(): 
    element = []
    for token in line.strip():
        data.append(token)


cpt = 0


#       sgrrrrwcrrlqqgppfg 




data.append('')
data.append('')
data.append('')
data.append('')

for a in data :
    print(a,cpt)
    if a != '':
        b = data[int(cpt)+1]
        print("b : ",b)
        if b != a :
            c = data[int(cpt)+2]
            print("c : ",c)
            if c != a and c != b :
                d = data[int(cpt)+3]
                print("d : ",d)
                if d != c and d != b and d != a :
                    print(a,b,c,d)
                    break
    cpt += 1
print("\n//////////////////////////////////////")
print("PART 1 :")      
print("Le résultat est : ", cpt+4) # +4 parce que le compteur s'incrémente a chaque itération de a mais on souhaite avoir la valeur a partir de d
print("//////////////////////////////////////\n\n")  
