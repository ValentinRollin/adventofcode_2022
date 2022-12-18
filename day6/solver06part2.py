with open('input_06.txt') as file:
    data = file.read()


cpt = 0
lettres = []

#       sgrrrrwcrrlqqgppfg 


print(data)

for a in range(14,len(data)) :
    sr = set(data[(a-14):a])
    if len(sr) == 14:
        print(sr)
        break
    #print(a,cpt)




print("\n//////////////////////////////////////")
print("PART 1 :")      
print("Le résultat est : ", a)
print("//////////////////////////////////////\n\n")  
