#Kevin Dooley 06 Mar 19
#write a program thats asks for a floating number
#returns dquare root of that number

#float was used instead of int because 
#we want a decimal number
#by using float, a decimal point will be always be returned
x = float(input("Enter a floating number"))

#Used the built in math function
#allows use to different mathematical functions#
#in this case we want to find the square root math.sqrt
#if program was longer, could shorten sqrt
#using from math import sqrt as sq

from math import sqrt
print(sqrt(x))