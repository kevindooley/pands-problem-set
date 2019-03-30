#Kevin Dooley 06 Mar 19
#write a program thats asks for a floating number
#returns dquare root of that number

#float was used instead of int because 
#we want a decimal number
#by using float, a decimal point will be always be returned

x = float(input("Please enter a positive floating number: "))

if x < 0:
    print("please enter a positive floating number")

#Used the built in math function
#allows use to different mathematical functions#
#in this case we want to find the square root math.sqrt
# shorten sqrt to sq - math import sqrt as sq

from math import sqrt
#while loop will run as long as x is a floating point number
#otherwise will break and go to print statment at the bottom 
while x != float:
    print("enter a decimal number")
    break
    
if  
#ans is square root in decimal form
    ans = sqrt(x)
#ans1 becomes approx square root using round
    ans1 = round(ans, 1)
    print("The square root of", x, "is approx", ans1)


    

