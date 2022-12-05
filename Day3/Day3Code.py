# --- Day 3: Rucksack Reorganization ---
# Each rucksack has two compartments


#Reading file
import os
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day3')
my_file = open("inputtext3.txt", "r")
inputcode = my_file.readlines()

#Creating a list of alphabet
alphabet = []
for i in range(97,(97+26)):
    alphabet.append(chr(i))

for j in range(65,(65+26)):
    alphabet.append(chr(j))


#Part 1
"""
for rucksacks in inputcode:
    
    priority_number = 1
    
    #Splitting string in half
    compartment_one = rucksacks[slice(0,len(rucksacks)//2)]
    compartment_two = rucksacks[slice(len(rucksacks)//2, len(rucksacks))]
    
    print(compartment_one,compartment_two)
    
    #Finding the common letter between the halfs
    common_item = ''.join(set(compartment_one).intersection(compartment_two))
"""  
sum_of_priorities = 0
#Part 2
#Finding the common letter between three lines. First compare line 1 and 2, then result against line 3.
for i in range(0,len(inputcode)-2,3):
    priority_number = 1
        
    intersection_one = ''.join(set(inputcode[i]).intersection(set(inputcode[i+1])))
    intersection_one = intersection_one.replace("\n","")
    
    common_item = ''.join(set(intersection_one).intersection(set(inputcode[i+2])))
    common_item = common_item.replace("\n","")
    
    
    #Finding the priority value by comparing the common letter through the alphabet created earlier
    for letter in alphabet:
    
        if letter == common_item:
            print("The priority number is: "+str(priority_number))
            sum_of_priorities += priority_number
    
        priority_number +=1    
print("The sum of priorities are: " + str(sum_of_priorities))

   
   
   
