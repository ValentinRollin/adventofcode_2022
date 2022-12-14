
# A = rock = 1 pts, B = paper = 2 pts, C = scissors = 3 pts
# X = loose = 0 pts, Y = draw = 3 pts, Z = win = 6 pts

file = open("input_02.txt")
data2 = []
for line in file.readlines(): 
    line = line.strip()
    score = 0
    #case A
    if line == 'A X':    
        score += 3 + 0
    if line == 'A Y':
        score += 1 + 3
    if line == 'A Z':
        score += 2 + 6
    #case B
    if line == 'B X':    
        score += 1 + 0
    if line == 'B Y':
        score += 2 + 3
    if line == 'B Z':
        score += 3 + 6
    #case C
    if line == 'C X':    
        score += 2 + 0
    if line == 'C Y':
        score += 3 + 3
    if line == 'C Z':
        score += 1 + 6
    data2.append(score)
print("//////////////////////////////////////")
print("PART 2 :")  
print("Le résultat 2 est : ", sum(data2))
print("//////////////////////////////////////\n\n")  