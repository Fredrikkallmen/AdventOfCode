#How many total Calories is that Elf carrying?

#Reading file
import os
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\Day1\Day1')
my_file = open("inputtext1.txt", "r")
inputcode = my_file.readlines()
inputcode.append('\n')


#Code
most_calories = 0
elf_calories = 0
calorie_list = []
for x in inputcode:
    
    if x != '\n':
        elf_calories = elf_calories + int(x)
    else:
        calorie_list.append(elf_calories)
        if elf_calories > most_calories:
            most_calories = elf_calories
            elf_calories = 0
        else:
            elf_calories = 0
            continue


sum_top_3, mx = 0,0

for i in range (3):
    mx = max(calorie_list)
    print(mx)
    sum_top_3 += mx
    calorie_list.remove(mx)
    
print("Most calories: " + str(most_calories))
print("The sum of the top three are: "+ str(sum_top_3))    
    
#How many Calories are those Elves carrying in total?