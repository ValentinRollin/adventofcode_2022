
file = open("input_06.txt")
data=[]

for line in file.readlines(): 
    element = []
    for token in line.strip():
        data.append(token)


cpt = 0
lettres = []


#       sgrrrrwcrrlqqgppfg 




data.append('')
data.append('')
data.append('')
data.append('')

for a in data :
    print(a,cpt)
    if a != '':
        if a not in lettres :  
            lettres.append(a)
            print("AJOUT : ",lettres)
        else :
            i = 0
            while( i <= len(lettres)) :
                print(i)  
                i+=1
                print("DELETE : ",lettres)    
    else : 
        break
    cpt += 1

print("\n//////////////////////////////////////")
print("PART 1 :")      
print("Le résultat est : ", cpt)
print("//////////////////////////////////////\n\n")  

print(lettres)