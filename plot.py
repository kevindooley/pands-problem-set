# Kevin Dooley 24 Mar 19
#plot a function

#import built in numpy as abbreviation 'np'
#import built in matplotlib.pyplot as 'plt' 
import numpy as np                  
import matplotlib.pyplot as plt     
#np.arrange returns evenly spaced values within a given interval, gives back array
#range of (0, 4) in step of 1. Step not required in this case - default is 1
x = np.arange(0, 4)                 
#name given to x axis
#name given to the y axis
plt.xlabel('x axis')                
plt.ylabel('y axis')                

#title function givens title of plot, loc givens position of title
# Given each function a variable name to use in the code
plt.title('Plot of three functions: x, x2 and 2x', loc='center')   

 # Given each function a variable name to use in the code
a = x                               
b = x**2
c = 2**x

# plot graphs the function, 'r--, b--, g--' - give colour of line and set to broken line
plt.plot(x, a, 'r--', x, b, 'b--', x, c, 'g--') # plot graphs the function, 'r--, b--, g--' - give colour of line and set to broken line

plt.show()