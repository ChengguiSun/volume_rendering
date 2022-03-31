"""
Read one .mat file and create a .mhd file with SimpleITK.
"""

import imp
import scipy.io
import SimpleITK as sitk
import os
from import_data import import_data
from filters import filters
from realignment import realignment


def mat2mhd(Path):
    """Convert a single .mat file to a single .mhd file."""

    old_name=os.path.basename(Path) # extract file name
    name = old_name.split('.')[0] # split name and file extension
    save_path = "../output" # define save folder path
    new_name = save_path + "/" + '{}.{}'.format(name, 'mhd') # new file name

    #import data and do the filtering
    Mocap, US_Stack = import_data(Path)
    filter_tog = {"M":0,"C":1,"H":0,"Q":0,"V":1,"G":1}
    filter_val = {"M":[1,1],"C":[0.6,0.8,0,1],"H":[1],"Q":[5,0.6],"G":[3]}

    for i in range(Mocap.shape[0]):
        US_Stack[:,:,i] = filters(US_Stack[:,:,i],filter_tog,filter_val)
    
    US_Stack = realignment(US_Stack,Mocap)

    # load data directly from preprocessed .mat file.
    # mat = scipy.io.loadmat(Path) 
    # arr = mat['AAA'][0,0][1] # key 'AAA' shall be updated with keys of various .mat files.

    # write and save .mhd file 
    img = sitk.GetImageFromArray(US_Stack)
    sitk.WriteImage(img, new_name)


def main():
    Path = 'F:/MM804/dataset/Code and Data for Students/Set 1/Neutral1/T3-NA.mat'

    mat2mhd(Path)

# Driver Code
if __name__ == '__main__':
   main()
