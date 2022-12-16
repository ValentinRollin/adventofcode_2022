file = open("input_03.txt")
data=[]
limit = ' '
caractere = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for line in file.readlines(): 
    element = []
    for token in line.strip().split(limit):
        data.append(token)
        print(data)

score = 0

for rucksack in data: 
    #case first compartment
    cpt1 = sorted(rucksack[:len(rucksack)//2])
    a=[]
    for x in cpt1 :
        if x not in a:
            a.append(x)

    #case second compartment
    cpt2 = sorted(rucksack[len(rucksack)//2:])
    b=[]
    for x in cpt2:
        if x not in b:
            b.append(x)

    #case comparison between compartment 1 & compartment 2 + score
    for char in a :
        if char in b:
          score +=caractere.index(char)+1 

          
print("\n//////////////////////////////////////")
print("PART 1 :")      
print("Le résultat est : ", score)
print("//////////////////////////////////////\n\n")  
