"""Render np.array volume with pyvista."""


import scipy.io
import SimpleITK as sitk
import pyvista as pv
import numpy as np

# import data from mat file
mat = scipy.io.loadmat('./Data/Code_and_Data_for_Students/Set1/Neutral1/T10-NA.mat')
arr = mat['Vertebra'][0,0][1]

print(arr.shape)
print(np.amax(arr))

# volume rendering with pyvista
data = pv.wrap(arr)
data.plot(volume=True)
