#Kevin Dooley 24th Feb 19
#Solution to question 1
#Write a program that asks the user to input any positive integer
#outputs outputs the sum of all numbers between one and that number

x = int(input("enter a positive number"))


#question asks for a positive number
#if statement to tell user to enter a number greater than 0
if x <= 0:
    print ("Please enter a positive number")

elif x > 0:
    total = int(x*(x+1)/2)
    print("The sum is", total)





