## Name   -  Chandra Prakash
## Reg No -  22-27-04
## Date     -  20 Oct 2022

## Program 1 - MP Model-Thresholding Logic

import numpy as np
np.random.seed(seed=0)
I = np.random.choice([0,1], 3)  # generate random vector I, sampling from {0,1}
W = np.random.choice([-1,1], 3) # generate random vector W, sampling from {-1,1}
print(f'Input vector:{I}, Weight vector:{W}') #Input vector:[0 1 1], Weight vector:[-1 1 1]
dot = I @ W
print(f'Dot product: {dot}') 
#Dot product: 2

def linear_threshold_gate(dot: int,T: float) -> int:
#Returns the binary threshold output
    if dot >= T:
        return 1
    else:
        return 0

T = 1
activation = linear_threshold_gate(dot, T)
print(f'Activation: {activation}')
#Activation: 1

T = 3
activation =linear_threshold_gate(dot, T)
print(f'Activation: {activation}')
#Activation: 0