"""
Read one .mat file and create a .mhd file with SimpleITK.
"""

import scipy.io
import SimpleITK as sitk

mat = scipy.io.loadmat('./Data/Code_and_Data_for_Students/Set1/Neutral1/T10-NA.mat')
arr = mat['Vertebra'][0,0][1]
img = sitk.GetImageFromArray(arr)
sitk.WriteImage(img, "./output/T10-NA.mhd")    # write and save .mhd file 
