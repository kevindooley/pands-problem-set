#Kevin Dooley 03 Mar 19
#Write a program that takes an input string
#Outputs every second word

a = input("Please type any sentence")

words = a.split()

new = ' '.join(words)


print(new[::2])



