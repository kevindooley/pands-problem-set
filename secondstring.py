#Kevin Dooley 03 Mar 19
#Write a program that takes an input string
#Outputs every second word


#ask the user to enter a word on the command line#
#stored as variable 'sentence'
sentence = input("Please type any sentence: ")

#used built in join & split functions
#created variable 'x' by spliting the initial string input from the user
#[start:stop:step] - we do not know what the user will enter so we have no start or end point
#split at every space and we want every second word so use slice of 2
#split function has turned variable 'sentence' into a list containing every second word
x = sentence.split(' ')[::2]

#created 3rd variable 'second_word' 
#used join function to turn list 'x' back to a string
#enter a string first - in this case a space (' ') because I want  a space between the words
#variable 'second_word' is now a string
second_word = ' '.join(x)
print(second_word)


