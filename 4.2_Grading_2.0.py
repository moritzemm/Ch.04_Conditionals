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
if FG >= 90:
    LG = "Your letter grade is A"
elif FG >= 80:
    LG = "Your letter grade is B"
elif FG >= 70:
    LG = "Your letter grade is C"
elif FG >= 60:
    LG = "Your letter grade is D"
else:
    LG = "You Should Transfer to Johnston!"
print("Which means",LG)
