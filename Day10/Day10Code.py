# --- Day 10: Cathode-Ray Tube ---
import os
import numpy
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day10')
lines = [line.strip().split(" ") for line in open('inputtext10.txt', 'r').readlines()]

sprite_array = []
for i in range(246):
    sprite_array.append(".")
sprite_array[0],sprite_array[1],sprite_array[2] = "#","#","#"
CRT_row = []

#print(sprite_array)
def solve_part1(lines,target_cycle):
    current_cycle = 0
    X = 1
    for line in lines:
        
        if line[0] == "noop":
            
            current_cycle = noop(current_cycle)
            
        if line[0] == "addx":
            
            X, current_cycle = addx(X,current_cycle,target_cycle,int(line[1]))

        if current_cycle == target_cycle:
            signal_strength = target_cycle * X
            break
    return signal_strength

def noop(current_cycle,row_tracker):
    
    if sprite_array[current_cycle] == "#":
            
            CRT_row.append("#")
        
    else:
            CRT_row.append(".")
            
    current_cycle += 1
    row_tracker += 1
    return current_cycle, row_tracker   
    
    
    
def addx(X,current_cycle,target_cycle,add_value):
    
    for i in range(2):
        current_cycle += 1
       #print(f"The current cycle is : {current_cycle}")
        if current_cycle == target_cycle:
            return X, current_cycle
    #print(f"Adding {add_value} to X")
    X += add_value
    #print(f"The value of X is {X}")
    return X, current_cycle


def solve_part2(lines):
    current_cycle = 0
    row_tracker = 0
    sprite_position = 1
    for line in lines:
        
        if line[0] == "noop":
            
            current_cycle, row_tracker = noop(current_cycle,row_tracker)
            
        if line[0] == "addx":
            
            sprite_position, current_cycle, row_tracker = move_sprite(sprite_position,current_cycle,int(line[1]),row_tracker)


    
    
        
def move_sprite(sprite_position,current_cycle, add_value,row_tracker):
    
    for i in range(2):
        
        if row_tracker > 39:
            #Deleting old
            sprite_array[sprite_position], sprite_array[sprite_position-1], sprite_array[sprite_position+1] = ".",".","."
            print(f"Increasing sprite position from {sprite_position} to {sprite_position+40}")
            sprite_position += 40
            row_tracker = 0
            
            #Adding new position
            sprite_array[sprite_position], sprite_array[sprite_position-1], sprite_array[sprite_position+1] = "#","#","#"
        
        if sprite_array[current_cycle] == "#":
            
            CRT_row.append("#")
        
        else:
            CRT_row.append(".")
            
        current_cycle += 1
        row_tracker += 1
    #Deleting old
    sprite_array[sprite_position], sprite_array[sprite_position-1], sprite_array[sprite_position+1] = ".",".","."
    
    #Adding new position
    sprite_position += add_value
    sprite_array[sprite_position], sprite_array[sprite_position-1], sprite_array[sprite_position+1] = "#","#","#"

    print(sprite_position)
    #print(current_cycle)
    #print(sprite_array)
    return sprite_position, current_cycle, row_tracker

#Part1:
#print("The sum of the signal strengths are: ")
#print(solve_part1(lines,20)+solve_part1(lines,60)+solve_part1(lines,100)+solve_part1(lines,140)+solve_part1(lines,180)+solve_part1(lines,220))

#Part2:
solve_part2(lines)
#for x in range(240):
#    CRT_row[x] = x
print(CRT_row[0:40])
print(CRT_row[40:80])
print(CRT_row[80:120])
print(CRT_row[120:160])
print(CRT_row[160:200])
print(CRT_row[200:240])



