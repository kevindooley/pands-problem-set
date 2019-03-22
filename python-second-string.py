#Kevin Dooley 03 Mar 19
#Write a program that takes an input string
#Outputs every second word

sentence = input("Please type any sentence")



new_sentence = ' '.join(sentence.split()[::2])
print (new_sentence)


