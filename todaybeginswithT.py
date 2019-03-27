#Kevin Dooley 24th Feb 19
#Solution question 2
#A Program that outputs what day it is
#whether today is a day that starts with a T


#Import is a bult in function that allows you to get basic date and time information from the computer
import datetime

#if statement used to see if condition is true
#each day of the week is represented by a number 
#when using weekday()
#0 = Monday, 1=Tuesday, 2=Wednes ...... up to 6 =Sunday
if datetime.datetime.today().weekday() == 1:
#indented to show print is part of above if statement
    print("Yes, Today starts with a T")


#same rationale as comments 10 to 13
if datetime.datetime.today().weekday() == 3:
    print("Yes, Today starts with a T")

#when the if statements dont apply
#because the above 'if' statements are not equal to 1 or 3
#else statement used to print saying today not day starting with T
else:
    print("No, today does not start with a T")
