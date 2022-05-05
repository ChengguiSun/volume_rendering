"""
Render volume with pyvista from an array.
"""


import scipy.io
import SimpleITK as sitk
import pyvista as pv
import numpy as np
from import_data import import_data
from filters import filters
from realignment import realignment
from import_and_preprocess import import_preprocess


# import and preprocess data from .mat file
US_Stack = import_preprocess('./Data/Code_and_Data_for_Students/Set1/Neutral1/T10-NA.mat')

# print(mat)
print(US_Stack.shape)
print(np.amax(US_Stack))

# volume rendering with pyvista
data = pv.wrap(US_Stack)
data.plot(volume=True, cmap=["silver"])
