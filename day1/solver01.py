
file = open("input_01.txt")
#data = file.read()
score = 0
data=[]


for line in file.readlines(): 
    line = line.strip()
    if line == '':    
        data.append(score)
        score = 0
    else :
        score += int(line)

print("\n//////////////////////////////////////")
print("PART 1 :")       
print ("Calories being carried by the Elf carrying the most calories are :", max(data))
print("//////////////////////////////////////\n\n")  
data = sorted(data)


print("//////////////////////////////////////")
print("PART 2 :")     
print ("The top3 Elves carrying the most calories are carrying in total :", data[-1] + data[-2] + data[-3])
print("//////////////////////////////////////\n\n")  
file.close()


