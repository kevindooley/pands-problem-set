#Kevin Dooley 03 Mar 19
#Create a program thats asks for a positive integer
#Determines if integer is prime or not


#question asks for a positive number
#used if statement incase negative no. used
#this tells the user to enter a number greater than 0
i = int(input("Enter a positive integer"))

if i < 2:
    print ("Please enter a new positve number")

for n in range(2, i):
        if i % n ==0:
            print(n, "is not a prime number")
            break

else:
    print(i, "is a prime number")


