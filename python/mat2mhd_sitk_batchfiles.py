"""
Read the .mat files in a folder and create .mhd files with files' old names.
The library used here is SimpleITK.
"""

import scipy.io
import SimpleITK as sitk
import os
from import_data import import_data
from filters import filters
from realignment import realignment

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

        #import data and do the filtering
        Mocap, US_Stack = import_data(path)
        filter_tog = {"M":0,"C":1,"H":0,"Q":0,"V":1,"G":1}
        filter_val = {"M":[1,1],"C":[0.6,0.8,0,1],"H":[1],"Q":[5,0.6],"G":[3]}

        for j in range(Mocap.shape[0]):
            US_Stack[:,:,j] = filters(US_Stack[:,:,i],filter_tog,filter_val)
    
        US_Stack = realignment(US_Stack,Mocap)

        # load data directly from preprocessed .mat file.
        # mat = scipy.io.loadmat(path) 
        # arr = mat['AAA'][0,0][1] # key 'AAA' shall be updated with keys of various .mat files.
        # arr = mat['Vertebra'][0,0][1]

        # write and save .mhd file 
        img = sitk.GetImageFromArray(US_Stack)
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
