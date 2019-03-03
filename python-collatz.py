#Kevin Dooley 03 Mar 19
#Write a program that asks the user to input any positive integer
# outputs the successive values of the below calculation

# calculate the next value by taking the current value
# divide it by two if it is even
#multiply it by three and add one if it is odd
#end the program when the current value is one

x = int(input("please enter a positive number"))

if x <= 0:
    print ("Please enter a positive number")

for i in range(x):
    if i % 2 ==0:
        print (i//2)

    elif i % 2 !=0:
        print ((i * 3) + 1)


        
    
