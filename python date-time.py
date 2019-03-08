#Kevin Dooley 08 Mar 19
#A program that outputs todays date and time
#Expressed in the format “Monday, January 10th 2019 at 1:15pm”

import datetime as dt
import calendar as cl


x = dt.datetime.now()
print(x)