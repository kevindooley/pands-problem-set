i = int(input("Enter a positive integer"))

if i < 0:
    print ("please enter a positve integer")

if i > 0 :
    if i % 1 !=0 or i % i !=0 or i % 2 ==0:
        print (i, "is not a prime number")

if i > 0:
    if i % 1 ==0 and i % i ==0 and i % 2 !=0:
        print(i, "is a prime number")

