## Name   -  Chandra Prakash
## Reg No -  22-27-04
## Date     -  20 Oct 2022

## Program 4 - Activation functions - Python
import matplotlib.pyplot as plt
import numpy as np

def binaryStep(x):
    ''' It returns '0' if the input is less then
    zero otherwise it returns one '''
    return np.heaviside(x,1)
x = np.linspace(-10, 10)
plt.plot(x, binaryStep(x))

plt.axis('tight')
plt.title('Activation Function :binaryStep')
plt.show()
def linear(x):
    ''' y = f(x) It returns the input as it is'''
    return x
plt.plot(x, linear(x))

