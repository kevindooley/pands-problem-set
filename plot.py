# Kevin Dooley 24 Mar 19
#plot a function

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4)

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('Plot of three functions: x, x2 and 2x', loc='center')

a = x
b = x**2
c = 2**x

plt.plot(x, a, 'r--', x, b, 'b--', x, c, 'g--')

plt.show()