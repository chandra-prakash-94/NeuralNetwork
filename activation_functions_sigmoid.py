## Name   -  Chandra Prakash
## Reg No -  22-27-04
## Date     -  20 Oct 2022

## Program 4 - Activation functions - Python
import matplotlib.pyplot as plt
import numpy as np
def sigmoid(x):
    ''' It returns 1/(1+exp(-x)). where the
    values lies between zero and one '''
    return 1/(1+np.exp(-x))
x = np.linspace(-10, 10)
plt.plot(x, sigmoid(x))
plt.axis('tight')
plt.title('Activation Function :sigmoid')
plt.show()
def tanh(x):
    ''' It returns the value (1-exp(-
    2x))/(1+exp(-2x)) and the value returned
    will be lies in between -1 to 1.'''
    return np.tanh(x)
plt.plot(x, tanh(x))

