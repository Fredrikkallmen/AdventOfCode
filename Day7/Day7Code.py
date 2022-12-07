# --- Day 7: No Space Left On Device ---
# Credit to TheRugbyOwl @ reddit for code
import os
import re
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day7')
#lines = [line.strip() for line in open('Inputtext7.txt', 'r').readlines()]
console = [i.split(" ") for i in list(open("Inputtext7.txt").read().rstrip().split("\n"))]

file_size = {}

parent_directories = []

current_directory =["/"]

def change_directory(input):
    
    if input == "..":
        current_directory[0] = parent_directories.pop(-1)
    else:
        parent_directories.append(current_directory[0])
        current_directory[0] = current_directory[0] + "/" + input
        #print("Current d: " +str(current_directory))
        #print("Parent d: " +str(parent_directories))
        

def update_fs(fs,file):
    
    if file in file_size:
        file_size[file] = file_size[file] + int(fs)
        #print("File size updated: "+ str(file_size))
    else:
        file_size[file] = int(fs)
        #print("New file size added: "+ str(file_size))

def process_line(line):
    
    if len(line) == 3: # A line with 3 parts is a change directory command
        #print("Change directory line detected")
        change_directory(line[2])
        
    elif bool(re.search("^\d+$",line[0])):
        update_fs(line[0],current_directory[0])
        for p in parent_directories:
            update_fs(line[0],p)



for line in console[1:]:
    print(line)
    process_line(line)

#print("Current directory: " + str(current_directory))
#print("Parent directory: " + str(parent_directories))
print(file_size)


under_100000_sum = 0
sorted_list = []
for size in file_size:
    print (file_size[size])
    if file_size[size] < 100000:
        under_100000_sum +=file_size[size]
    sorted_list.append(file_size[size])
    
print("The total sum of all files under size 100000 is : "+ str(under_100000_sum))

#Part 2
size_surplus = (int(file_size["/"])-40000000)
print("Total size of disk: 70000000 and the current total size is "+ str(file_size["/"])+ " and the total free space need to be 3000000, therefore we need to free at least "+str(size_surplus)+" amount of space")

sorted_list.sort()
print(sorted_list)
for lowest_number in sorted_list:
    
    if lowest_number > size_surplus:
        #print(lowest_number)
        print("Directory: " + str(list(file_size.keys())[list(file_size.values()).index(lowest_number)]) +" will be deleted and save up to " + str(lowest_number)+ " in space")
        break

