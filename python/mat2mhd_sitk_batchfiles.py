"""
Read the .mat files in a folder and create .mhd files with files' old names.
The library used here is SimpleITK.
"""

import scipy.io
import SimpleITK as sitk
import os

# Define a function to convert .mat files to .mhd files
def mat2mhd(filePaths):
    """ Read the .mat files in a folder and create .mhd files 
        with the old names."""

    for i, path in enumerate(filePaths, 1):
        print('-- processing %d/%d' % (i, len(filePaths)))
        old_name=os.path.basename(path) # extract file name
        name = old_name.split('.')[0] # split name and file extension
        print(name) # print names and track the process
        save_path = "./output" # define save folder path
        new_name = save_path + "/" + '{}.{}'.format(name, 'mhd') # new file name
        # new_name = save_path + "/" + '{}.{}'.format(name, 'mha')
        mat = scipy.io.loadmat(path) 
        # arr = mat['AAA'][0,0][1] # key 'AAA' shall be updated with keys of various .mat files.
        arr = mat['Vertebra'][0,0][1]
        # write and save .mhd file 
        img = sitk.GetImageFromArray(arr)
        sitk.WriteImage(img, new_name)

# Define a main function to build filepaths from a folder path
def main():
    filePaths = []
    # for root, __, files in os.walk('./Data/PhantomSpine/Group1/2019-04-18-IRExperiment2/1-Neutral'):
    for root, __, files in os.walk('./Data/Code_and_Data_for_Students/Set1/Neutral1'):
        for f in files:
            if f.endswith(".mat"):
                filePaths.append(os.path.join(root, f))

    mat2mhd(filePaths)

# Driver Code
if __name__ == '__main__':
   main()
