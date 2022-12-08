#--- Day 8: Treetop Tree House ---
import numpy
import os
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day8')
lines = [line.strip() for line in open('inputtext8.txt', 'r').readlines()]



#Creating a matrix
def matrix_creation(input):
    size = len(input)
    matrix = numpy.zeros((size,size),dtype=int)
    j=0
    for row in input:
        for i in range(len(input)):
            matrix[j][i] = row[i]
        j += 1   
    #print(matrix)     
    return matrix


#Going through all trees inside the outer square and checking against nearby trees if it is larger
def check_visibility(input_matrix):
    scenic_view_best = 0
    scenic_view_rating = 0
    
    total_visibile_trees = (len(input_matrix)*len(input_matrix)) - ((len(input_matrix)-2)*(len(input_matrix)-2))
    #print("Length is : " +str(len(input_matrix)))
    for i in range(1,len(input_matrix)-1):
    
        for j in range(1,len(input_matrix)-1):
            visibility = 0
            scenic_view_rating = 0
            #Checking directions: up, right, down, left
            #Up
            visibility_up, scenic_view_rating_up = check_up(input_matrix,i,j)
            #Down
            visibility_down, scenic_view_rating_down = check_down(input_matrix,i,j)
            #Right
            visibility_right, scenic_view_rating_right = check_right(input_matrix,i,j)
            #Left
            visibility_left, scenic_view_rating_left = check_left(input_matrix,i,j)
            
            visibility = visibility_down+visibility_left+visibility_right+visibility_up
            scenic_view_rating = scenic_view_rating_down*scenic_view_rating_left*scenic_view_rating_right*scenic_view_rating_up
            
            if visibility > 0:
                total_visibile_trees += 1
            if scenic_view_rating > scenic_view_best:
                scenic_view_best = scenic_view_rating
            
    return total_visibile_trees,scenic_view_best        
            
            
def check_up(input_matrix,x,y):
    visibility = 1
    scenic_view_rating = 0
    #print("Checked position is " +str(x)+ ","+str(y) + " and is the number: "+ str(input_matrix[x][y]))           
    for i in range(1,x+1):
        
        if input_matrix[x][y] > input_matrix[x-i][y]:
        
            #print("Checked position " + str(input_matrix[x][y]) + " is larger than " + str(input_matrix[x-i][y]) +", "+ str(i) + " step above")
            visibility = 1
            scenic_view_rating += 1
        else:
            #print("This tree is blocked from the north by another tree in position: ("+ str(x)+", "+str(y-i)+") with a height of "+ str(input_matrix[x-i][y]))   
            visibility = 0
            scenic_view_rating += 1
            break
    #print("Scenic rating: "+ str(scenic_view_rating))
    return visibility, scenic_view_rating        

def check_down(input_matrix,x,y):
    visibility = 1
    scenic_view_rating = 0
    #print("Checked position is " +str(x)+ ","+str(y) + " and is the number: "+ str(input_matrix[x][y]))           
    for i in range(1,len(input_matrix)-x):
        
        if input_matrix[x][y] > input_matrix[x+i][y]:
        
            #print("Checked position " + str(input_matrix[x][y]) + " is larger than " + str(input_matrix[x+i][y]) +", "+ str(i) + " step below")
            visibility = 1
            scenic_view_rating += 1
        else:
            #print("This tree is blocked from the south by another tree in position: ("+ str(y+i)+", "+str(x)+") with a height of "+ str(input_matrix[x+i][y]))   
            visibility = 0
            scenic_view_rating += 1
            break
    #print("Scenic rating: "+ str(scenic_view_rating))
    return visibility, scenic_view_rating 

def check_right(input_matrix,x,y):
    visibility = 1
    scenic_view_rating = 0
    #print("Checked position is " +str(x)+ ","+str(y) + " and is the number: "+ str(input_matrix[x][y]))           
    for i in range(1,len(input_matrix)-y):
        
        if input_matrix[x][y] > input_matrix[x][y+i]:
        
            #print("Checked position " + str(input_matrix[x][y]) + " is larger than " + str(input_matrix[x][y+i]) +", "+ str(i) + " step to the right")
            visibility = 1
            scenic_view_rating += 1
        else:
            #print("This tree is blocked from the east by another tree in position: ("+ str(y)+", "+str(x+i)+") with a height of "+ str(input_matrix[x][y+i]))   
            visibility = 0
            scenic_view_rating += 1
            break
    #print("Scenic rating: "+ str(scenic_view_rating))
    return visibility, scenic_view_rating 

def check_left(input_matrix,x,y):
    visibility = 1
    scenic_view_rating = 0
    #print("Checked position is " +str(x)+ ","+str(y) + " and is the number: "+ str(input_matrix[x][y]))           
    for i in range(1,y+1):
        
        if input_matrix[x][y] > input_matrix[x][y-i]:
        
            #print("Checked position " + str(input_matrix[x][y]) + " is larger than " + str(input_matrix[x][y-i]) +", "+ str(i) + " step to the left")
            visibility = 1
            scenic_view_rating += 1
        else:
            #print("This tree is blocked from the west by another tree in position: ("+ str(y)+", "+str(x-i)+") with a height of "+ str(input_matrix[x][y-i]))   
            visibility = 0
            scenic_view_rating += 1
            break
    #print("Scenic rating: "+ str(scenic_view_rating))
    return visibility, scenic_view_rating              
            
#check_up(matrix_creation(lines),3,2)
#check_down(matrix_creation(lines),3,2)
#check_right(matrix_creation(lines),3,2)
#check_left(matrix_creation(lines),3,2)
print(check_visibility(matrix_creation(lines)))