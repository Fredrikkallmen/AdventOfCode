#--- Day 12: Hill Climbing Algorithm ---
import numpy
import os
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day12')

lines = [line.strip("\n") for line in open("inputtext12.txt","r").readlines()]

print(lines[0][0])

current_position = (0,0)
print(int(chr("E")))