# 2019 Programming and Scripting Problem Sets

This repository (pands-problem-set) contains all my solutions and comments to the problem set 2019 for the module Programming and Scripting.
[See link for instructions on completing the problem set] https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf

The problem set is due the 31st of March 19 and the pands-problem-set repository URL is to be submitted on Moodle.

# Getting Started/Prerequisites.

1. If not already installed, download and install Python 3.
2. Recommend downloading python via Anaconda to get useful additional software, including Visual Studio Code and Ipython.
3. Download and install a command prompt - recommend Cmder (Windows) or Terminal (Mac).
4. Download the files from this repository to your desktop.

#How to run the files.

1. Open the command prompt and change directory to the location you saved the files.
2. See below for title of solution 1 and open it on the command line.
3. Complete above step for all 10 solutions.

#Question 1 - sumupto.py

Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

This program will ask the user to enter a positive number on the command line and subsequently print the sum of all numbers between one and that number. I used an 'if' statement in this program to tell the user to enter a positive number and try again if a number less than zero is entered. The 'elif' statement was then used to run the program if the correct conditions were met i.e. positve number entered.
I used a mathematical formula to calculate the sum in this solution, following research I found the the Gauss formula calculates the sum of a series.

Lecture Material Used for Solution:
Week 4 - controlling the flow, conditionals if, elif and else

References and additional resoures:
http://mathcentral.uregina.ca/qq/database/qq.02.06/jo1.html
https://docs.python.org/3/tutorial/controlflow.html
https://www.w3schools.com/python/python_conditions.asp

#Question 2 - todaybeginswithT.py

Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is as follows.

This program tells the user whether today is a day that begins with the letter T. If the current day is a Tuesday or a Thursday, the program will print 'Yes, Today starts with a T' otherwise will print 'No, today does not start with a T'.
The built in datetime module was imported for this program. Ran 'if' conditionals to see if today started with a T while date.weekday() was instead of date. isoweekday(). An 'else' conditional used to print if today did not begin with a T.

Lecture Material used for Solution:
Week 4 - controlling the flow, 'conditionals if, elif and else'
Week 2 -thinking like a programmer,'your first program'.

References and additional resoures:
https://docs.python.org/3/library/datetime.html#datetime.date.weekday
https://docs.python.org/3/library/datetime.html#available-types
https://www.w3schools.com/python/python_datetime.asp
