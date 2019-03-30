#Kevin Dooley 11 Mar 19
#Write a program that reads a text file
#outputs every second line


#import sys - this nuilt in module allows you to take argurments from the command line
import sys

#program will run if there are 2 filenames on the command line
#otherwise else conditional will ask user to try again
if len(sys.argv) == 2:

#Used recommended 'with' function to open text file - called text file as 'f'
#by using 'with' and indenting my code
#there is no need to use 'close()' to close the file
#the file automatically closes once the loop has finished.
#by using sys.argv[1], the program will open the 2nd filename on the command line and run the below code
    with open(sys.argv[1], 'r') as f:


#created variable 'x' to be used in for loop
#'x' will be iterated through the loop until there are no more lines left in the text file
        x = 0

        for line in f:
#'x' iterated by 1 until no more lines in the text file
            x+=1

#'if' statement in the for loop because indented
#'if' statement says - if x divided by 2 does not give a remainder 
#print that line
#I have set the program to print the odd lines of the text.
            if x % 2 != 0:
#end="" set to nothing and this will remove default \n or end of line or space.
                print(line, end="")

else:
    print("Please provide two filenames on the command line to run this program")

