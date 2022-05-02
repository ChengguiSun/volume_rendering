"""
Read one .mat file and create a .mhd file with SimpleITK.
"""

import imp
from importlib.resources import path
import scipy.io
import SimpleITK as sitk
import os
from import_data import import_data
from filters import filters
from realignment import realignment
from import_and_preprocess import import_preprocess


def mat2mhd(Path):
    """Convert a single .mat file to a single .mhd file."""

    old_name=os.path.basename(Path) # extract file name
    name = old_name.split('.')[0] # split name and file extension
    save_path = "../output" # define save folder path
    new_name = save_path + "/" + '{}.{}'.format(name, 'mhd') # new file name

    # preprocess data
    US_Stack = import_preprocess(Path)
    
    # write and save .mhd file 
    img = sitk.GetImageFromArray(US_Stack)
    sitk.WriteImage(img, new_name)


def main():
    Path = 'F:/MM804/dataset/Code and Data for Students/Set 1/Neutral1/T10-NA.mat'

    mat2mhd(Path)

# Driver Code
if __name__ == '__main__':
   main()
