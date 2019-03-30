#Kevin Dooley 06 Mar 19
#write a program thats asks for a floating number
#returns dquare root of that number

#float was used instead of int because 
#we want a decimal number
#by using float, a decimal point will be always be returned

x = float(input("Please enter a positive floating number: "))

#Used the built in math function
#allows use to different mathematical functions#
#in this case we want to find the square root math.sqrt
# shorten sqrt to sq - math import sqrt as sq
from math import sqrt

#asks user to try again if negative number entered
if x <= 0:
    print("Please enter a positive decimal number")

#asks user to try again if a floating number is not entered
if x > 0 and x == int(x):
        print("Please try again and enter a decimal number")
        
#runs below code is number entered is a decimal number
elif x > 0 and x == float(x):
#ans = the square root of x in decimal form
        ans = sqrt(x)
#ans_1 becomes approx square root (to 1 decimal place) using round function
        ans_1 = round(ans, 1)
        print("The square root of", x, "is approx", ans_1)


    

