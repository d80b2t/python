'''
  Day 2: Operators

  Objective 
  In this challenge, you''ll work with arithmetic operators. Check out
  the Tutorial tab for learning materials and an instructional video!
  
'''

mealCost   = float(input()) 
tipPercent = int(input())   
taxPercent = int(input()) 

tip = mealCost * (tipPercent/100.)
tax = mealCost * (taxPercent/100.)

totalCost = mealCost + tip + tax
total = round(totalCost)

print ('The total meal cost is', int(total), 'dollars.')
