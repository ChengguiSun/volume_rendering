"""
Render volume with pyvista from an array.
"""


import scipy.io
from scipy.ndimage import gaussian_filter
import SimpleITK as sitk
import pyvista as pv
import numpy as np
from import_data import import_data
from filters import filters
from realignment import realignment


# import data from mat file
Mocap, US_Stack = import_data('./Data/Code_and_Data_for_Students/Set1/Neutral1/T10-NA.mat')
filter_tog = {"M":0,"C":1,"H":0,"Q":0,"V":1,"G":1}
filter_val = {"M":[1,1],"C":[0.6,0.8,0,1],"H":[1],"Q":[5,0.6],"G":[3]}

for i in range(Mocap.shape[0]):
    US_Stack[:,:,i] = filters(US_Stack[:,:,i],filter_tog,filter_val)
    
US_Stack = realignment(US_Stack,Mocap)

# print(mat)
print(US_Stack.shape)
print(np.amax(US_Stack))

# volume rendering with pyvista
data = pv.wrap(US_Stack)
data.plot(volume=True, cmap=["silver"])
