import matplotlib.pyplot as plt
import numpy as np


# Heron's method for computing square roots

def heron(x0,S, n=0,iterates=None):
    '''
    intput:
        x the initial guess (positive)
        S the number we want to take the root of
        n counter for number of iterations
    output: 
       array
        array of iterates starting at x0

        end element of the array gives you an approixmation of the square root of S

    '''
    if iterates is None:
        iterates = [x0]

    if(n > 10):
        return np.array(iterates)
    else:
        x_next = (S + x0**2)/(2*x0)
        iterates.append(x_next)
        return heron(x_next, S, n+1, iterates)
        

print(heron(1,2))

# Graphing the error.

S= 10000
x0 = 20000

xpoints = heron(x0,S)
ypoints = np.abs(xpoints - np.sqrt(S))

plt.plot(xpoints, ypoints)
plt.show()
