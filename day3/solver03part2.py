file = open("input_03.txt")
data=[]
limit = ' '
caractere = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for line in file.readlines(): 
    element = []
    for token in line.strip().split(limit):
        data.append(token)


score = 0

for rucksack in range(len(data)//3): 
    #case line 1
    cpt1 = sorted(data[rucksack*3])
    a=[]
    for x in cpt1 :
        if x not in a:
            a.append(x)
    #case line 2
    cpt2 = sorted(data[3*rucksack+1])
    b=[]
    for x in cpt2:
        if x not in b:
            b.append(x)
    #case line 3
    cpt3 = sorted(data[3*rucksack+2])
    c=[]
    for x in cpt3:
        if x not in c:
            c.append(x)
    #case comparison between 3 lines + score
    for char in a :
        if char in b:
            if char in c:
                score +=caractere.index(char)+1 

print("//////////////////////////////////////")
print("PART 2 :")  
print("Le résultat 2 est : ",score)
print("//////////////////////////////////////\n\n")  