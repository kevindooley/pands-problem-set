#Kevin Dooley 08 Mar 19
#A program that outputs todays date and time
#Expressed in the format “Monday, January 10th 2019 at 1:15pm”


#datetime module allows representation of date and time
#shortened datetime to dt to reduce number of characters
import datetime as dt


#strftime allows user to return date in string format
#import datetime module, within that use sub section datetime and then sub section strftime
#%A = Day of week, %B = Month, %d = day of month, %Y = year, %I = hour, %M = minute, %p = AM/PM
today = dt.datetime.strftime(dt.datetime.now(), "%A, %B %dth %Y at %I:%M%p")
print (today)