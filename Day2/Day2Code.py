#What would your total score be if everything goes exactly according to your strategy guide?
# Strategy - A/X: Rock [1], B/Y: Paper [2], C/Z: Scissor [3]
#Total Score = sum of scores each round. Score each round = pick of hand + win/loss/draw
#Win = 6p , Draw = 3p Lose = 0p

#Reading file
import os
os.chdir(r'C:\Users\FredrikKällménESSIQ\Desktop\Python\AdventOfCode\AdventOfCode\Day2')
my_file = open("inputtext2.txt", "r")
inputcode = my_file.readlines()

#Scorecard
points = { "Rock":1 , "Paper":2 , "Scissor":3}

#What to pick depending on move and what opponent plays
lose = {"A":"Scissor", "B":"Rock", "C":"Paper"}
draw = {"A":"Rock", "B":"Paper", "C":"Scissor"}
win = {"A":"Paper", "B":"Scissor", "C":"Rock"}

"""
inputcode = [
"A Y",
"B X",
"C Z"
]
"""

#Variables
round_score = 0
total_score = 0

for combination in inputcode:
    
    #Splitting
    opponent_hand, winning_move = combination.split()
    

    
    #Picking if to lose/draw/win and choosing hand
    if winning_move == "X":
        my_hand = lose[opponent_hand]
    elif winning_move == "Y":
        my_hand = draw[opponent_hand]
    elif winning_move == "Z":
        my_hand = win[opponent_hand]
      
    #Losing scenarios // No points added
    if my_hand == "Rock" and opponent_hand == "B":
        round_score += 0
    elif my_hand == "Paper" and opponent_hand == "C":
        round_score += 0
    elif my_hand == "Scissor" and opponent_hand == "A":
        round_score += 0
    
    #Winning scenarios // 6 points for victory added
    elif my_hand == "Rock" and opponent_hand == "C":
        round_score += 6
    elif my_hand == "Paper" and opponent_hand == "A":
        round_score += 6
    elif my_hand == "Scissor" and opponent_hand == "B":
        round_score += 6
        
    #All other combinations are draws // 3 points for draw
    else:
        round_score += 3
        
    #Adding points for my selected hand // 1p for rock, 2p for paper and 3p for scissor
    round_score += points[my_hand]
    
    #Summarize and reset round
    total_score += round_score
    round_score = 0
    
     
print("The total score of the rock&paper&scissor game is: " + str(total_score))
