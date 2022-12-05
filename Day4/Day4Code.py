# --- Day 4: Camp Cleanup ---

#Reading file
import os
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day4')
my_file = open("inputtext4.txt", "r")
inputcode = my_file.readlines()

number_of_assignments_overlap_fully = 0
number_of_assignments_overlap_partly = 0

for pairs in inputcode:
    elf1_sections = []
    elf2_sections = []
    #Splitting up the pair
    elf1,elf2 = pairs.split(",")
    #print(elf1,elf2)    
    
    elf1_section1, elf1_section2 = elf1.split("-")
    elf2_section1, elf2_section2 = elf2.split("-")
    
    #Creating numbers
    for i in range(int(elf1_section1),int(elf1_section2)+1):
        
        elf1_sections.append(str(i))
    #print("Section 1: "+str(elf1_sections))
    for j in range(int(elf2_section1),int(elf2_section2)+1):
        
        elf2_sections.append(str(j))
    #print("Section 2: "+str(elf2_sections))
    
    #Checking each number in list against each number in other list. The amount of matches should be equal to either length of list for a success
    match_number = 0
    for x in elf1_sections:
        for y in elf2_sections:
            if x == y:
                match_number += 1
                overlapped = 1
                
    if match_number == len(elf1_sections) or match_number == len(elf2_sections):
        number_of_assignments_overlap_fully += 1  
    if overlapped == 1:
        number_of_assignments_overlap_partly += 1
        overlapped = 0
 
            
print("Number of assignments that fully overlap: "+ str(number_of_assignments_overlap_fully))
print("Number of assignments that fully overlap: "+ str(number_of_assignments_overlap_partly))