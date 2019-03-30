#Kevin Dooley 03 Mar 19
#Write a program that asks the user to input any positive integer
# outputs the successive values of the below calculation

# calculate the next value by taking the current value
# divide it by two if it is even
#multiply it by three and add one if it is odd
#end the program when the current value is one
x = int(input("Please enter a positive number: "))


#defining function - function called collatz
def collatz(n):

#print the first number in the function collatz
#end=' ' allows a space after print instead of a new line character. Allows user to continue on the same line
    print(n, end=' ')

#while loop will continue to keep looping as long as n is not equal to 1
    while n != 1:

#if n is an even number
        if n % 2 == 0:

#n is  divided by 2 (runs on if statement because it is indented)
            n = n // 2
            print(n, end=' ')

#if the number is not even if must be odd
#else statement run within while loop
        else:

#n becomes (n multiplied by 3) + 1
            n = (n * 3) + 1
            print(n, end=' ')
#call function   
collatz(x) 


    
    

        
    
