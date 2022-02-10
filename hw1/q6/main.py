import numpy as np

# Sample input 2d array
a = np.arange(12)
a = a.reshape(2,6) 

# 6.1
def function_1(array_input) :
    for r in array_input:
        for c in r:
            print(c, end = " ")
        print()

# 6.2
def function_2(array_input) :
    output = array_input.ravel('F')
    print(output)

function_2(a) # Check how it works

# 6.3
def function_3(array_input) :
    output = np.where(array_input<0, 0, array_input)
    print(output)

function_3(a)

# 6.4
def function_4(array_input) :
    output = array_input.reshape(3,4)
    print(output)

function_4(a)

# 6.5
def function_5(array_input) :
    output = np.around(array_input, 2)
    print(output)

function_5(a)    