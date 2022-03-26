"""
Read one .mat file and create a .mhd file with SimpleITK.
"""

import scipy.io
import SimpleITK as sitk
import os


def mat2mhd(Path):
    """Convert a single .mat file to a single .mhd file."""

    old_name=os.path.basename(Path) # extract file name
    name = old_name.split('.')[0] # split name and file extension
    save_path = "./output" # define save folder path
    new_name = save_path + "/" + '{}.{}'.format(name, 'mhd') # new file name
    mat = scipy.io.loadmat(Path) 
    # arr = mat['AAA'][0,0][1] # key 'AAA' shall be updated with keys of various .mat files.
    arr = mat['Vertebra'][0,0][1]
    # write and save .mhd file 
    img = sitk.GetImageFromArray(arr)
    sitk.WriteImage(img, new_name)


def main():
    Path = './Data/Code_and_Data_for_Students/Set1/Neutral1/T10-NA.mat'

    mat2mhd(Path)

# Driver Code
if __name__ == '__main__':
   main()
