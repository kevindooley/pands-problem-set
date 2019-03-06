#Kevin Dooley 03 Mar 19
#Create a program thats asks for a positive integer
#Determines if integer is prime or not


#question asks for a positive number
#used if statement incase number less that 2 is used
#this tells the user to enter a number greater than 2
#because anything less than 2 isnt a prime number
i = int(input("Enter a positive integer"))

    
#for statement used so there is a looping sequence
#until the indented statements are false
#range function only starts at 2 because 2 is the 1st prime number
#i is the inputed integer#
#i in the range function is upto but not including i
for n in range(2, i):
    if i < 0:
        break
#if statement within for loop
#a prime number can only be divided by 1 & itself
#i % n ==0 means any number that gives no remainder it divides into i
#it cannot be a prime number
    if i % n ==0:
        print(i, "is not a prime number")
#break statement used within for loop
#the break statement means the for loop is broken when 
#the if statement above it is no longer true
        break

#because the break statement has broken the loop
#the else statement now kicks in outside of the for loop
else:
    if i > 0:
#i did not meet the criteria set in the for loop
        print(i, "is a prime number")

    else: 
        if i < 0:
            print("A positive integer is required, Try again")





