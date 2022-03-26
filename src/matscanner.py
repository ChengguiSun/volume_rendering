"""
Print the keys of a .mat file and get the dimension of arrays.
"""

import scipy.io

# import data from mat file
mat = scipy.io.loadmat('./Data/PhantomSpine/Group1/2019-04-18-IRExperiment2/1-Neutral/T5NA.mat')
# arr = mat['AAA'][0,0][1]
# arr = mat['Vertebra'][0,0][1]

# print(mat)
print("keys: ",mat.keys())
print("shape of mat['AAA'][0,0][0]: ", mat['AAA'][0,0][0].shape)
print("shape of mat['AAA'][0,0][1]: ", mat['AAA'][0,0][1].shape)
