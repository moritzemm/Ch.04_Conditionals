'''
NUMBER ANALYSIS PROGRAM
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''
print("Welcome to the number analysis program!")
N=int(input("What number should I analyze? "))
if N%2==0 :
    print("Your number is Even")
else :
    print("Your number is Odd")
print ()
if N >= 0 :
    print("Your number is Positive")
elif N==0 :
    print("Your number is zero")
else:
    print("Your number is Negative")
print()
if N >=-100 and N<=100:
    print("Your number is Inclusive")
else :
    print("Your number is Exclusive")
print()