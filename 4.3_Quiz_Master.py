'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
must ask 7 questions, must print grade at the end, must be able to add questions and the grade be calculated
must say correct or not after each question, have nice spacing,
'''
print("~Welcome to the basic welding quiz~")
Ts=0

A = input("1. What type of welding is most commonly used in industries?\nA. Tig\nB. Mig\nC. Gas\n")
if A.lower() == "a" or A.lower() == "tig" or A.lower() == "c" or A.lower()== "gas":
    print("Wrong the right answer was B")
elif A.lower() == "b" or A.lower() == "mig":
    print("Correct!")
    Ts+=1
else :
    print("Not a choice")
print()

A= input("2. What type of gas welding is most commonly used?\nA. Oxygen\nB. Natural\nC. Oxy-acetylene\n")
if A.lower() == "a" or A.lower() == "oxygen" or A.lower() == "b" or A.lower()== "natural":
    print("Wrong the right answer was C")
elif A.lower() == "c" or A.lower() == "oxy-acetylene":
    print("Correct!")
    Ts+=1
else :
    print("Not a choice")
print()

A= input("3. What is the most commonly used rod when stick/arc welding?\nA. 7018\nB. 6034\nC. 8094\n")
if A.lower() == "b" or A.lower() == "6034" or A.lower() == "c" or A.lower()== "8094":
    print("Wrong the right answer was A")
elif A.lower() == "a" or A.lower() == "7018":
    print("Correct!")
    Ts+=1
else :
    print("Not a choice")
print()

A= input("4. Why must we wear safty glasses when in the welding shop?\nA. Because sparks fly and could get into your eyes\nB. Because they look cool\nC. You don't\n")
if A.lower() == "b" or A.lower() == "c" or A.lower() == "because they look cool" or A.lower()== "you don't":
    print("Wrong the right answer was A")
elif A.lower() == "a" or A.lower() == "because sparks fly and could get into your eyes":
    print("Correct!")
    Ts+=1
else :
    print("Not a choice")
print()

A= input("5. Why do we have to wear gloves when welding?\nA. To keep us warm\nB. To protect from cuts\nC. To protect us from sparks and heat\n")
if A.lower() == "a" or A.lower() == "b" or A.lower() == "to keep us warm" or A.lower()== "to protect from cuts":
    print("Wrong the right answer was C")
elif A.lower() == "c" or A.lower() == "to protect us from sparks and heat":
    print("Correct!")
    Ts+=1
else :
    print("Not a choice")
print()

A= input("6. Do you cover your hair when welding?\nA. Yes, with a hat or bandana\nB. Yes, with your hand\nC. No\n")
if A.lower() == "b" or A.lower() == "c" or A.lower() == "yes, with your hand" or A.lower()== "no":
    print("Wrong the right answer was A")
elif A.lower() == "a" or A.lower() == "yes, with a hat, or bandana":
    print("Correct!")
    Ts+=1
else :
    print("Not a choice")
print()

A= input("7. What must you do before you start so you get the electrical currect needed for your welder to work?\nA. Rub your socks on the carpet\nB. Ground the work piece\nC. Nothing just start\n")
if A.lower() == "a" or A.lower() == "c" or A.lower() == "rub your socks on the carpet" or A.lower()== "nothing just start":
    print("Wrong the right answer was B")
elif A.lower() == "b" or A.lower() == "ground the work piece":
    print("Correct!")
    Ts+=1
else :
    print("Not a choice")
print()

print("Your final score is",Ts)
print("Good Job!")

