'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print("Welcome to your Grade Calculator")
SG=int(input("What is your Semester grade?"))
FEG=int(input("What is your final exam grade?"))
FEW=int(input("What is your final exam worth?"))
FEW/=100
FG=SG*(1-FEW)+(FEG*FEW)
print("Your overall grade will be",FG)