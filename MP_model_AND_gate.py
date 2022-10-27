## Name   -  Chandra Prakash
## Reg No -  22-27-04
## Date     -  20 Oct 2022

## Program 2 - McCulloch Pitts Model- AND gate
# matrix of inputs
import numpy as np
input_table = np.array([
                        [0,0], # both no
                        [0,1], # one no, one yes
                        [1,0], # one yes, one no
                        [1,1]  # both yes
                        ])
print(f'input table:\n{input_table}')
weights = np.array([1,1])              # array of weights 
print(f'weights: {weights}')
dot_products = input_table @ weights   # dot product matrix of inputs and weights
print(f'Dot products: {dot_products}')
#Dot products: [0 1 1 2]

def linear_threshold_gate(dot: int,T: float) -> int:
#Returns the binary threshold output
    if dot >= T:
        return 1
    else:
        return 0

T = 2
for i in range(0,4):
    activation = linear_threshold_gate(dot_products[i], T)
    print(f'Activation: {activation}')
# Activation: 0
# Activation: 0
# Activation: 0
# Activation: 1

