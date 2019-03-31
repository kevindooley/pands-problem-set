# 2019 Programming and Scripting Problem Sets

This repository (pands-problem-set) contains all my solutions and comments to the problem set 2019 for the module Programming and Scripting.
- See link for instructions on completing the problem set - https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf

The problem set is due the 31st of March 19 and the pands-problem-set repository URL is to be submitted on Moodle.

# Getting Started/Prerequisites.

1. If not already installed, download and install Python 3.
2. Recommend downloading python via Anaconda to get useful additional software, including Visual Studio Code and Ipython.
3. Download and install a command prompt - recommend Cmder (Windows) or Terminal (Mac).
4. Download the files from this repository to your desktop.

# How to run the files.

1. Open the command prompt and change directory to the location you saved the files.
2. See below for title of solution 1 and open it on the command line.
3. Complete step 2 above for all 10 solutions.

# Question 1 - sumupto.py

**Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.**

This program will ask the user to enter a positive number on the command line and subsequently print the sum of all numbers between one and that number. I used an 'if' statement in this program to tell the user to enter a positive number and try again if a number less than zero is entered. The 'elif' statement was then used to run the program if the correct conditions were met i.e. positve number entered.
I used a mathematical formula to calculate the sum in this solution, following research I found the the Gauss formula calculates the sum of a series.

###### Lecture Material Used for Solution:
Week 4 - controlling the flow, conditionals if, elif and else

###### References and additional resoures:
- http://mathcentral.uregina.ca/qq/database/qq.02.06/jo1.html
- https://docs.python.org/3/tutorial/controlflow.html
- https://www.w3schools.com/python/python_conditions.asp

# Question 2 - todaybeginswithT.py

**Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is as follows.**

This program tells the user whether today is a day that begins with the letter T. If the current day is a Tuesday or a Thursday, the program will print 'Yes, Today starts with a T' otherwise will print 'No, today does not start with a T'.
The built in datetime module was imported for this program. Ran 'if' conditionals to see if today started with a T while date.weekday() was used instead of date.isoweekday(). An 'else' conditional used to print if today did not begin with a T.

###### Lecture Material used for Solution:
- Week 4 - controlling the flow, 'conditionals if, elif and else'
- Week 2 -thinking like a programmer

###### References and additional resoures:
- https://docs.python.org/3/library/datetime.html#datetime.date.weekday
- https://docs.python.org/3/library/datetime.html#available-types
- https://www.w3schools.com/python/python_datetime.asp

# Question 3 - divisors.py

**Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.**

This program will print out on the command line all the numbers in the range of 1000 to 10000 that can be divided by the number 6 evenly but not the number 12 evenly.
To determine the range between the above numbers I used the built in range function within a for loop. The 'if' conditional was then used within the 'for' loop of the specific range. The modulus operator determined if each number within the range could be divided by 6 but not 12.

###### Lecture Material used for Solution:
- Week 4 - controlling the flow: 'conditionals if, elif and else'
- Week 4 - Loops: 'while and for'

###### References and additional resoures:
- https://docs.python.org/3/tutorial/controlflow.html#for-statements
- https://docs.python.org/3/tutorial/controlflow.html#the-range-function
- https://www.w3schools.com/python/python_for_loops.asp
- https://www.youtube.com/watch?v=HWcs5qdvvo0
- https://stackoverflow.com/a/30462892

# Question 4 - collatz.py

**Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.**

I used the defining function to complete this question. Within the 'def' function I created a while loop to keep looping until the conditional I set was no longer true. An 'if' conditional was used to determine if a number was even and if it was even it was divided by two. The 'else' conditonal was used for odd numbers, they were multiplied by three, plus one. This kept running until the calculation reached number one.

###### Lecture Material used for Solution:
- Week 4 - Controlling the flow: 'conditionals if, elif and else'
- Week 4 - Loops: 'while and for'
- Week 6 - Reusing code: 'functions'

###### References and additional resoures:
- https://www.youtube.com/watch?v=9Os0o3wzS_I
- https://www.w3schools.com/python/python_functions.asp
- https://stackoverflow.com/a/35417009
- https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- https://en.wikipedia.org/wiki/Collatz_conjecture
- https://docs.python.org/3/whatsnew/3.0.html#print-is-a-function

# Question 5 - primes.py

**Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.**

The program will first ask the user to enter a positive number on the command line. Using a 'for' loop and the built in 'range' function, a range between two and the number user enters will be looped. There is are three statements with the 'if' conditional within the 'for' loop and if any of the three are met the loop will break and ask the user to try again because they didnt meet the criteria of the question.
'If' and 'else' conditionals used to see if number prime or not within range of 'for' loop.

###### Lecture Material used for Solution:
- Week 4 - Controlling the flow: 'conditionals if, elif and else'
- Week 4 - Loops: 'while and for'
- Week 4 - Controlling loops: 'continue and break'

###### References and additional resoures:
- https://www.programiz.com/python-programming/break-continue
- https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

# Question 6 - secondstring.py
**Write a program that takes a user input string and outputs every second word.**

This program will ask the user to type a sentence onto the command line. The program will then output every second word of that original sentence. To achieve this I used both the built in 'split' and 'join' functions. By using split, the original sentence will be in a list containing every second word. Join will then convert that list back into a string, separated by a blank space.

###### Lecture Material used for Solution:
Week 7 - Files: 'string operations'

###### References and additional resoures:
- https://docs.python.org/3/library/stdtypes.html#str.split
- https://docs.python.org/3/library/stdtypes.html#str.join
- https://www.w3schools.com/python/python_strings.asp
- https://stackoverflow.com/a/54857233
- https://www.youtube.com/watch?v=fc9buLUiqLE

# Question 7 - squareroot.py

**Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.**

The program will ask the user to enter a positive decimal number on the command line. It will then calculate the square root of that number to 1 decimal place. In this program I imported math and imported the squareroot module within math. An 'if' statement was used to investigate if the user had entered positive number, if they hadnt they would be prompted to try again. Another 'if' statement was used incase a whole number was entered on the command line, they are once again prompted to try again. The 'elif' conditional was used when the correct condtions were met and then the square root would be calculated. The round function ensured the answer was to one decimal place as per in the question.

###### Lecture Material used for Solution:
- Week 6 - Reusing code: 'modules'
- Week 4 - Controlling the flow: 'conditionals if, elif and else'

###### References and additional resoures:
- https://www.tutorialspoint.com/python3/python_modules.htm
- https://www.geeksforgeeks.org/python-math-function-sqrt/
- https://docs.python.org/3/library/math.html#module-math
- https://www.programiz.com/python-programming/methods/built-in/round

# Question 8 - datetime.py

**Write a program that outputs today’s date and time in the format “Monday, January 10th 2019 at 1:15pm”.**

This program will tell the user the current date and time in the above format. Firstly I imported datetime and then used strftime module to pull the required information and formatting from datetime. Using strftime allows the program to output the date in the requested format.

###### Lecture Material used for Solution:
- Week 6 - Reusing code: 'modules'
- Week 2 -thinking like a programmer

###### References and additional resoures:
- https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
- https://www.w3schools.com/python/python_datetime.

# Question 9 - second.py
**Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.**

This program will read a text file from an argument on the command line. The program will output every second line of the text file. 
To do this I first had to import sys to allow the user to take an arugument from the commant line. There is an 'if' conditional that will only allow the program to run if there are two filenames on the command line. This program outputs the contents of a text file so there is a text file saved in the same folder so that is possible. To open the file in read I used 'with' so there is no need to manually close the text file after it has run. Sys.argv within the 'with' function means that the text file will run and an 'if' conditional in the code ensures every second line of the text file is printed.

###### Lecture Material used for Solution:

- Week 4 - Controlling the flow: 'conditionals if, elif and else'
- Week 7 - Files: 'Opening files for reading and writing'
- Week 9 - Interactive Python for data analysis: 'Command line arguments'

###### References and additional resoures:

- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- https://stackoverflow.com/a/7439162
- https://www.poftut.com/python-how-to-print-without-newline-or-space/
- https://docs.python.org/3/library/sys.html#sys.argv

# Question 10 - plot.py

**Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].**

In this program I have imported mathplotlib.pyplot which will create the plot for the above functions while numpy was also imported as it is required to be able to add the range. The plot will also have a title in the centre and an x and y axis. Each function on the plot will be differenciated by 3 separate colours.

###### Lecture Material used for Solution:
- Week 9 - Interactive Python for data analysis: 'Matplotlib and Pyplot'
- Week 9 - Interactive Python for data analysis: 'Numpy'

###### References and additional resoures:
- https://matplotlib.org/users/pyplot_tutorial.html
- https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
- https://www.tutorialspoint.com/numpy/numpy_matplotlib.htm

