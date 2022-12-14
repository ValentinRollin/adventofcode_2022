# A = Rock = X = 1 pts
# B = Paper = Y = 2 pts 
# C = Scissors = Z = 3 pts
# loose = 0 pts, draw = 3 pts, win = 6 pts


file = open("input_02.txt")
data=[]

for line in file.readlines(): 
    line = line.strip()
    score = 0
    #case A
    if line == 'A X':    
        score += 1 + 3
    if line == 'A Y':
        score += 2 + 6
    if line == 'A Z':
        score += 3 + 0
    #case B
    if line == 'B X':    
        score += 1 + 0
    if line == 'B Y':
        score += 2 + 3
    if line == 'B Z':
        score += 3 + 6
    #case C
    if line == 'C X':    
        score += 1 + 6
    if line == 'C Y':
        score += 2 + 0
    if line == 'C Z':
        score += 3 + 3
    data.append(score)

print("\n//////////////////////////////////////")
print("PART 1 :")      
print("Le résultat est : ", sum(data))
print("//////////////////////////////////////\n\n")  
