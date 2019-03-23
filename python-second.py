#Kevin Dooley 11 Mar 19
#Write a program that reads a text file
#outputs every second line


#Used recommended 'with' function to open text file - called text file as 'f'
#by using 'with' and indenting my code
#there is no need to use 'close()' to close the file
#the file automatically closes once the loop has finished.
with open('myfile.txt', 'r') as f:

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
            print(line)

        

        




   