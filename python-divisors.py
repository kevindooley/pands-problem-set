#Kevin Dooley 02 Mar 19
#A program thats prints all numbers between 1000 & 10000
#that are divisable by 6 but not by 12


#i is the number at any given time with the 'for' loop
#the 'for' loop iterates through the algorithim in the given range
#using the range of 1000 to 10000 and then stops [Start:Stop:Step]
#range funtion used to set numbering start and end point

#this range starts at 1000, stops at but does not include 10000
#stepping/incrementing in 1 - no step mentioned, automatically 1
for i in range( 1000, 10000):

#indented as part of for loop
#as the number must be divisible by 6
#arithmetic operator %(modulo of a number) means dividing it by that number 
#and have a remainder of 0 ie gives a whole number
#comparision operator == means equal to 

    if i % 6 ==0 and i % 12 !=0:
#the number cannot be divisable by 12
#same as line 21 except comparision operator !=0 (not equal to 0)
#if i is divided by 12 and has a remainder it is to be excluded from the answer
        print(i)


