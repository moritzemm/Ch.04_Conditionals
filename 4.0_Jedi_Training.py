# Sign your name:___Emma_Moritz___

  #1. Make the following program work. (There's 3 mistakes)

midichlorians=float(input("Enter midichlorian count: "))
if midichlorians>10000:
 print("You have serious Jedi potential")
else:
  print("Jedi, you will never be.")

 # 2. Make the following program work. 3
     
x = int(input("Enter a number: "))
if x ==3:
    print("You entered 3")


  # 3. Make the following program work. 4
     
a = input("What is the name of Poe Dameron's Droid? ")
if a == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. 4
     
x = input("Name one of the top 3 greatest Jedi.")
if x == "Yoda" or x=="Luke Skywalker" or x=="Obi-Wan Kenobi":
print ("That is correct!")



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master.
# print("Not a choice") if they don't enter any of the 3 an set sensitivity to blank text.

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character: ")

if user_input.lower() == "a" :
         sensitivity = 1000
elif user_input.lower() == "b" :
         sensitivity = 900
elif user_input.lower() == "c" :
         sensitivity = 0
else:
    print("Not a choice")

print("Sensitivity: ",sensitivity)
