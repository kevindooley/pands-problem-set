#Kevin Dooley 24th Feb 19
#Solution to question 1
#Write a program that asks the user to input any positive integer
#outputs the sum of all numbers between one and that number

x = int(input("enter a positive number"))


#question asks for a positive number
#used if statement incase negative no. used
#this tells the user to enter a number greater than 0
if x < 0:
    print ("Please enter a positive number")

#if else statement used if numbered entered above 0
#researched mathematical formula that calculates sum of any integer

elif x > 0:
#discover gauss formula to caluclate the sum of
    total = int(x*(x+1)/2)
    print("The sum is", total)





