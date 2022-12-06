# --- Day 6: Tuning Trouble ---

#Reading file
import os
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day6')
my_file = open("inputtext6.txt", "r")
inputcode = my_file.readlines()


current_sequence = []
marker = 0

for sequence in inputcode:
    
    #Going through all letters. Changing between 4 and 14 depending on marker or message. Part 1 and part 2
    for i in range(14,len(sequence)):
        
        #Adding i and the three letters before into a sequence and making it into a set
        for j in range(14,0,-1):
            
            current_sequence.append(sequence[i-j])
            
        #If the set has shrunk to < 4, it means there were doubles
        if len(set(current_sequence)) == 14:
            
            marker = i
            break
            
        current_sequence = []   
                  
        
print("The amount of characters needed before finding the marker: " + str(marker)) 