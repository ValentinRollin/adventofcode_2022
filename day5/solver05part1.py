import re

file = open("input_05.txt")
data=[]
limit = ' '

for line in file.readlines()[10:]: 
    element = []
    for token in line.strip().split(limit):
        element.append(token)
    data.append(element)


#   [N]     [C]                 [Q]    
#   [W]     [J] [L]             [J] [V]
#   [F]     [N] [D]     [L]     [S] [W]
#   [R] [S] [F] [G]     [R]     [V] [Z]
#   [Z] [G] [Q] [C]     [W] [C] [F] [G]
#   [S] [Q] [V] [P] [S] [F] [D] [R] [S]
#   [M] [P] [R] [Z] [P] [D] [N] [N] [M]
#   [D] [W] [W] [F] [T] [H] [Z] [W] [R]
#    1   2   3   4   5   6   7   8   9 

one = ['N','W','F','R','Z','S','M','D']
two = ['S','G','Q','P','W']
three = ['C','J','N','F','Q','V','R','W']
four = ['L','D','G','C','P','Z','F']
five = ['S','P','T']
six = ['L','R','W','F','D','H']
seven = ['C','D','N','Z']
eight = ['Q','J','S','V','F','R','N','W']
nine = ['V','W','Z','G','S','M','R']




for a in data :
    nbr = a[1]
    cpt = 0
    de = a[3]
    vers = a[5]
    while(int(nbr) > 0) :

        #case from 1
        if de == '1' :
            if vers == '2' :
                two.insert(0,one[0])
                one.remove(one[0])
            if vers == '3' :
                three.insert(0,one[0])
                one.remove(one[0])
            if vers == '4' :
                four.insert(0,one[0])
                one.remove(one[0])
            if vers == '5' :
                five.insert(0,one[0])
                one.remove(one[0])
            if vers == '6' :
                six.insert(0,one[0])
                one.remove(one[0])
            if vers == '7' :
                seven.insert(0,one[0])
                one.remove(one[0])
            if vers == '8' :
                eight.insert(0,one[0])
                one.remove(one[0])
            if vers == '9' :
                nine.insert(0,one[0])
                one.remove(one[0])

        #case from 2
        if de == '2' : 
            if vers == '1' :
                one.insert(0,two[0])
                two.remove(two[0])
            if vers == '3' :
                three.insert(0,two[0])
                two.remove(two[0])
            if vers == '4' :
                four.insert(0,two[0])
                two.remove(two[0])
            if vers == '5' :
                five.insert(0,two[0])
                two.remove(two[0])
            if vers == '6' :
                six.insert(0,two[0])
                two.remove(two[0])
            if vers == '7' :
                seven.insert(0,two[0])
                two.remove(two[0])
            if vers == '8' :
                eight.insert(0,two[0])
                two.remove(two[0])
            if vers == '9' :
                nine.insert(0,two[0])
                two.remove(two[0])
        
        #case from 3
        if de == '3' : 
            if vers == '1' :
                one.insert(0,three[0])
                three.remove(three[0])
            if vers == '2' :
                two.insert(0,three[0])
                three.remove(three[0])
            if vers == '4' :
                four.insert(0,three[0])
                three.remove(three[0])
            if vers == '5' :
                five.insert(0,three[0])
                three.remove(three[0])
            if vers == '6' :
                six.insert(0,three[0])
                three.remove(three[0])
            if vers == '7' :
                seven.insert(0,three[0])
                three.remove(three[0])
            if vers == '8' :
                eight.insert(0,three[0])
                three.remove(three[0])
            if vers == '9' :
                nine.insert(0,three[0])
                three.remove(three[0])

        #case from 4
        if de == '4' : 
            if vers == '1' :
                one.insert(0,four[0])
                four.remove(four[0])
            if vers == '2' :
                two.insert(0,four[0])
                four.remove(four[0])
            if vers == '3' :
                three.insert(0,four[0])
                four.remove(four[0])
            if vers == '5' :
                five.insert(0,four[0])
                four.remove(four[0])
            if vers == '6' :
                six.insert(0,four[0])
                four.remove(four[0])
            if vers == '7' :
                seven.insert(0,four[0])
                four.remove(four[0])
            if vers == '8' :
                eight.insert(0,four[0])
                four.remove(four[0])
            if vers == '9' :
                nine.insert(0,four[0])
                four.remove(four[0])

        #case from 5
        if de == '5' : 
            if vers == '1' :
                one.insert(0,five[0])
                five.remove(five[0])
            if vers == '2' :
                two.insert(0,five[0])
                five.remove(five[0])
            if vers == '3' :
                three.insert(0,five[0])
                five.remove(five[0])
            if vers == '4' :
                four.insert(0,five[0])
                five.remove(five[0])
            if vers == '6' :
                six.insert(0,five[0])
                five.remove(five[0])
            if vers == '7' :
                seven.insert(0,five[0])
                five.remove(five[0])
            if vers == '8' :
                eight.insert(0,five[0])
                five.remove(five[0])
            if vers == '9' :
                nine.insert(0,five[0])
                five.remove(five[0])

        #case from 6
        if de == '6' : 
            if vers == '1' :
                one.insert(0,six[0])
                six.remove(six[0])
            if vers == '2' :
                two.insert(0,six[0])
                six.remove(six[0])
            if vers == '3' :
                three.insert(0,six[0])
                six.remove(six[0])
            if vers == '4' :
                four.insert(0,six[0])
                six.remove(six[0])
            if vers == '5' :
                five.insert(0,six[0])
                six.remove(six[0])
            if vers == '7' :
                seven.insert(0,six[0])
                six.remove(six[0])
            if vers == '8' :
                eight.insert(0,six[0])
                six.remove(six[0])
            if vers == '9' :
                nine.insert(0,six[0])
                six.remove(six[0])

        #case from 7
        if de == '7' : 
            if vers == '1' :
                one.insert(0,seven[0])
                seven.remove(seven[0])
            if vers == '2' :
                two.insert(0,seven[0])
                seven.remove(seven[0])
            if vers == '3' :
                three.insert(0,seven[0])
                seven.remove(seven[0])
            if vers == '4' :
                four.insert(0,seven[0])
                seven.remove(seven[0])
            if vers == '5' :
                five.insert(0,seven[0])
                seven.remove(seven[0])
            if vers == '6' :
                six.insert(0,seven[0])
                seven.remove(seven[0])
            if vers == '8' :
                eight.insert(0,seven[0])
                seven.remove(seven[0])
            if vers == '9' :
                nine.insert(0,seven[0])
                seven.remove(seven[0])

        #case from 8
        if de == '8' : 
            if vers == '1' :
                one.insert(0,eight[0])
                eight.remove(eight[0])
            if vers == '2' :
                two.insert(0,eight[0])
                eight.remove(eight[0])
            if vers == '3' :
                three.insert(0,eight[0])
                eight.remove(eight[0])
            if vers == '4' :
                four.insert(0,eight[0])
                eight.remove(eight[0])
            if vers == '5' :
                five.insert(0,eight[0])
                eight.remove(eight[0])
            if vers == '6' :
                six.insert(0,eight[0])
                eight.remove(eight[0])
            if vers == '7' :
                seven.insert(0,eight[0])
                eight.remove(eight[0])
            if vers == '9' :
                nine.insert(0,eight[0])
                eight.remove(eight[0])

        #case from 9
        if de == '9' : 
            if vers == '1' :
                one.insert(0,nine[0])
                nine.remove(nine[0])
            if vers == '2' :
                two.insert(0,nine[0])
                nine.remove(nine[0])
            if vers == '3' :
                three.insert(0,nine[0])
                nine.remove(nine[0])
            if vers == '4' :
                four.insert(0,nine[0])
                nine.remove(nine[0])
            if vers == '5' :
                five.insert(0,nine[0])
                nine.remove(nine[0])
            if vers == '6' :
                six.insert(0,nine[0])
                nine.remove(nine[0])
            if vers == '7' :
                seven.insert(0,nine[0])
                nine.remove(nine[0])
            if vers == '8' :
                eight.insert(0,nine[0])
                nine.remove(nine[0])
        nbr = int(nbr)-1
    #print(a)

print("one : ",one,'\n')
print("two : ",two,'\n')
print("three : ",three,'\n')
print("four : ",four,'\n')
print("five : ",five,'\n')
print("six : ",six,'\n')
print("seven : ",seven,'\n')
print("eight : ",eight,'\n')
print("nine : ",nine,'\n')

solution = one[0], two[0],three[0],four[0],five[0],six[0],seven[0],eight[0],nine[0]

    

   # print("test separateur",cpt1[1])


print("\n//////////////////////////////////////")
print("PART 1 :")      
print("Le résultat est : ", solution)
print("//////////////////////////////////////\n\n")  

