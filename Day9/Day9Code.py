#--- Day 9: Rope Bridge ---
#data = [int(x) for x in open("text6.txt").read().strip().split(",")]
import os
import numpy as np
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day9')

lines = [line.strip() for line in open('inputtext9.txt', 'r').readlines()]

matrix_size = 500
matrix  = np.empty((matrix_size,matrix_size),dtype=str) # Create a 6x6 matrix with "." elements
matrix.fill(".")
visited_matrix = np.zeros((matrix_size,matrix_size),dtype=int)
matrix_length = len(matrix)

#starting positions for H and T
H_x = int(matrix_length/2)
H_y = int(matrix_length/2)

T_x = int(matrix_length/2)
T_y = int(matrix_length/2)
current_coordinate_T = (T_x,T_y)
current_coordinate_H = (H_x,H_y)
matrix[H_x][H_y] = "H"


print("Starting array: \n" + str(matrix))
#print("Commands: " + str(lines))



def tail_catch_up(current_coordinate_H, previous_coordinate_H,current_coordinate_T):
    
    print(f"Head current coordinate: {current_coordinate_H}, head previous coordinate: {previous_coordinate_H} Tail current coordinate: {current_coordinate_T}")
    
    if current_coordinate_H == current_coordinate_T:
        print("Tail is under the Head")
        current_coordinate_T = current_coordinate_T
        matrix[current_coordinate_H[0]][current_coordinate_H[1]] = "H"
        coordinates_visited(current_coordinate_T)
        
    elif abs(current_coordinate_H[0] - current_coordinate_T[0]) < 2 and abs(current_coordinate_H[1] - current_coordinate_T[1]) < 2: #If distance to Heads is 1 it just keeps its position
        
        print("Tail is next to Head")
        matrix[current_coordinate_T[0]][current_coordinate_T[1]] = "T"
        current_coordinate_T = current_coordinate_T
        coordinates_visited(current_coordinate_T)
        
   
    else: #If distance is more than 1, T takes H's previous position
        
        print("Moving Tail to :" + str(previous_coordinate_H))
        
        matrix[previous_coordinate_H[0]][previous_coordinate_H[1]] = "T"
        matrix[current_coordinate_T[0]][current_coordinate_T[1]] = "."
        
        current_coordinate_T = previous_coordinate_H
        coordinates_visited(current_coordinate_T)
        
        print("Curr coord T :" + str(current_coordinate_T))
         
    return current_coordinate_T
    
    

def read_commands(direction,distance,current_coordinate_H, current_coordinate_T):
    #current_coordinate_H = (H_x,H_y)
    #current_coordinate_T = (T_x,T_y)
    #for command in command_list:
    #print("Current command: " + command)
        
        
    if direction == "U":
            print("Going up")
            current_coordinate_H, current_coordinate_T = going_up(distance,current_coordinate_H,current_coordinate_T)
    if direction == "R":
            print("Going right")
            current_coordinate_H, current_coordinate_T = going_right(distance,current_coordinate_H,current_coordinate_T)
    if direction == "D":
            print("Going down")
            current_coordinate_H, current_coordinate_T = going_down(distance,current_coordinate_H,current_coordinate_T)
    if direction == "L":
            print("Going left")
            current_coordinate_H, current_coordinate_T = going_left(distance,current_coordinate_H,current_coordinate_T)
    
    return current_coordinate_H, current_coordinate_T
        
def going_up(steps,current_coordinate_H,current_coordinate_T):

    for number_of_steps in range(int(steps)):
        
        print(f"H have moved: {abs(number_of_steps)} steps")
        
        previous_coorinate = (current_coordinate_H[0],current_coordinate_H[1])
        next_coordinate = (current_coordinate_H[0]-1,current_coordinate_H[1])
        
        matrix[next_coordinate[0]][next_coordinate[1]] = "H"
        matrix[previous_coorinate[0]][previous_coorinate[1]] = "."
        
        current_coordinate_H = next_coordinate
        
        current_coordinate_T = tail_catch_up(current_coordinate_H,previous_coorinate,current_coordinate_T)
        
        #print(matrix)
       
    return current_coordinate_H, current_coordinate_T
 
def going_right(steps,current_coordinate_H,current_coordinate_T):
    
    for number_of_steps in range(int(steps)):
        
        
        print(f"H have moved: {abs(number_of_steps)} steps")
        
        previous_coorinate = (current_coordinate_H[0],current_coordinate_H[1])
        next_coordinate = (current_coordinate_H[0],current_coordinate_H[1]+1)
        
        matrix[next_coordinate[0]][next_coordinate[1]] = "H"
        matrix[previous_coorinate[0]][previous_coorinate[1]] = "."
        
        current_coordinate_H = next_coordinate
        
        current_coordinate_T = tail_catch_up(current_coordinate_H,previous_coorinate,current_coordinate_T)
        
        #print(matrix)  
            
    return current_coordinate_H, current_coordinate_T

def going_down(steps,current_coordinate_H,current_coordinate_T):
    
    for number_of_steps in range(int(steps)):
    
        print(f"H have moved: {abs(number_of_steps)} steps")
        
        previous_coorinate = (current_coordinate_H[0],current_coordinate_H[1])
        next_coordinate = (current_coordinate_H[0]+1,current_coordinate_H[1])
        
        matrix[next_coordinate[0]][next_coordinate[1]] = "H"
        matrix[previous_coorinate[0]][previous_coorinate[1]] = "."
        
        current_coordinate_H = next_coordinate
        
        current_coordinate_T = tail_catch_up(current_coordinate_H,previous_coorinate,current_coordinate_T)
        
        #print(matrix)

    return current_coordinate_H, current_coordinate_T

def going_left(steps,current_coordinate_H,current_coordinate_T):
    
    for number_of_steps in range(int(steps)):
        
        
        
        print(f"H have moved: {abs(number_of_steps)} steps")
        
        previous_coorinate = (current_coordinate_H[0],current_coordinate_H[1])
        next_coordinate = (current_coordinate_H[0],current_coordinate_H[1]-1)
        
        matrix[next_coordinate[0]][next_coordinate[1]] = "H"
        matrix[previous_coorinate[0]][previous_coorinate[1]] = "."
        
        current_coordinate_H = next_coordinate
        
        current_coordinate_T = tail_catch_up(current_coordinate_H,previous_coorinate,current_coordinate_T)
        
        #print(matrix)
            
    return current_coordinate_H, current_coordinate_T

def coordinates_visited(coord):
    
    visited_matrix[coord[0]][coord[1]] = 1
    


      

#read_commands(lines)
#print(visited_matrix, visited_matrix.sum())
#print(visited_matrix[T_x][T_y])
#print(visited_matrix[T_x+1][T_y-1])



for command in lines:
    print("Current command: " + command)
    direction, distance = command.split(" ")
    print(direction,distance)
    current_coordinate_H, current_coordinate_T = read_commands(direction, distance,current_coordinate_H, current_coordinate_T)

print(visited_matrix, visited_matrix.sum())
#print(visited_matrix[T_x][T_y])
#print(visited_matrix[T_x+1][T_y-1])
"""
import numpy as np


def move(knots, move):
	knots[0] += move

	for prev_knot, curr_knot in zip(knots, knots[1:]):
		if max(abs(prev_knot - curr_knot)) > 1:
			curr_knot += np.clip((prev_knot - curr_knot), -1, 1)


def solve(x, k):
	knots = [np.array([0, 0]) for _ in range(k)]
	positions = set()
	shift = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L':(0, -1)}

	for line in x:
		direc, steps = line.split(" ")
		for _ in range(int(steps)):
			move(knots, shift[direc])
			positions.add(tuple(knots[-1]))

	return len(positions)


x = open("inputtext9.txt").readlines()

print(solve(x, 2))
print(solve(x, 10))

"""