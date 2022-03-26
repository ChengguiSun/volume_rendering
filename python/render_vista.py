"""
Render volume with pyvista from an array.
"""


import scipy.io
from scipy.ndimage import gaussian_filter
import SimpleITK as sitk
import pyvista as pv
import numpy as np


# import data from mat file
mat = scipy.io.loadmat('./Data/PhantomSpine/Group1/2019-04-18-IRExperiment2/1-Neutral/T5NA.mat')
arr = mat['AAA'][0,0][1]
# arr_denoise = np.zeros_like(arr)
# for i in range(arr.shape[2]):
#     arr_denoise[:,:,i] = gaussian_filter(arr[:,:,i], sigma=1)

# print(mat)
print(arr.shape)
print(np.amax(arr))

# volume rendering with pyvista
data = pv.wrap(arr)
data.plot(volume=True)
