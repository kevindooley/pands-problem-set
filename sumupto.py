#Kevin Dooley 24th Feb 19
#Solution to question 1
#Write a program that asks the user to input any positive integer
#outputs the sum of all numbers between one and that number

x = int(input("Please enter a positive number: "))


#question asks for a positive number
#used if statement incase negative no. used
#this tells the user to enter a number greater than 0 if initial input < 0
if x < 0:
    print ("Please enter a positive number: ")

#if else statement used if numbered entered above 0
#researched mathematical formula that calculates sum of any integer

elif x > 0:
#discovered gauss formula to calculate the sum of any integer
#this formula allows the user to find the sum of a series
#it is a very useful formula as you do not neead to manually add up every number
    sum = int(x*(x+1)/2)

#print the 'The sum is' string and the sum of the number
    print("The sum is", sum)





