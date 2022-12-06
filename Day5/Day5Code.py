#--- Day 5: Supply Stacks ---

#Reading file
import os
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day5')
my_file = open("inputtext5.txt", "r")
inputcode = my_file.readlines()

import array

#All possible columns where crates can be placed.
#      Bottom ---------------------------------------------Top
# 1
# 2
# 3
# Cont.

box_array = [
            ["N", "B", "D", "T", "V", "G", "Z", "J"],
            ["S", "R", "M", "D", "W", "P", "F"],
            ["V", "C", "R", "S", "Z"],
            ["R", "T", "J", "Z", "P", "H", "G"],
            ["T", "C", "J", "N", "D", "Z", "Q", "F"],
            ["N", "V", "P", "W", "G", "S", "F", "M"],
            ["G", "C", "V", "B", "P", "Q"],
            ["Z", "B", "P", "N"],
            ["W", "P", "W"]
            ]


for movement in inputcode:
    
    #Splitting the command sentence into a list. [1] how many we move, [3] from where, [5] and to which position
    movement = movement.split()
    how_many = int(movement[1]) #1
    from_where = int(movement[3])-1 #1
    to_where = int(movement[5])-1 #0
    
    #print(how_many,from_where,to_where)
    
    
    #Part 1 - CrateMover 9000
    """    
    #Doing movement of boxes
    for i in range(0,int(how_many)):
        
        print("Moving "+str(how_many)+" box from " + str(from_where) + " to " + str(to_where))
        #Copying a box to "to_where" from "from_where"
        box_array[to_where].append(box_array[from_where][len(box_array[from_where])-1])
        
        #Removes the box just taken
        del box_array[from_where][len(box_array[from_where])-1]
    """  
    #Part 2 - CrateMover 9001
    #Doing movement of boxes
    print(box_array)
    for i in range(int(how_many),0,-1):
        
        
        print("Moving "+str(how_many)+" box from " + str(from_where) + " to " + str(to_where))
        
        #Copying a box to "to_where" from "from_where"
        box_array[to_where].append(box_array[from_where][len(box_array[from_where])-i])
        
        
    #Removes the box just taken   
    for j in range(0,how_many):
        del box_array[from_where][len(box_array[from_where])-1]
    
    print(box_array)    



print(box_array)

final_combination = ""
for k in range(0,9):
    final_combination += box_array[k][len(box_array[k])-1]

print(final_combination)
