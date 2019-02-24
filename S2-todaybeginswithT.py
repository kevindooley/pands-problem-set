#Kevin Dooley 24th Feb 19
#A Program that outputs what day it it
#whether today is a day that starts with a T

import datetime

if datetime.datetime.today().weekday() == 1:
    print("Today starts with a T")

if datetime.datetime.today().weekday() == 3:
    print("Today starts with a T")

else:
    print("today does not start with a T")
