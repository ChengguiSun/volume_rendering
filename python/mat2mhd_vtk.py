"""
Write .mat file to MetaImage using vtk and numpy.
The .mhd files created by this method don't work very well with 3D slicer. 
"""

import numpy as np
import scipy.io
import vtk
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
data_arr = US_Stack.astype(np.uint8)  # uint8 max value 255

# imports raw data and stores it.
dataImporter = vtk.vtkImageImport()
data_string = data_arr.tobytes() # array is converted to a string of chars and imported.
dataImporter.CopyImportVoidPointer(data_string, len(data_string)) # Import data and make an internal copy
dataImporter.SetDataScalarTypeToUnsignedChar() # data set to unsigned char (uint8)
dataImporter.SetNumberOfScalarComponents(1) 
dataImporter.SetDataExtent(0, 479, 0, 639, 0, 1199) # 3d dimension
dataImporter.SetWholeExtent(0, 479, 0, 639, 0, 1199)

writer = vtk.vtkMetaImageWriter()
writer.SetFileName("T10-NA.mhd")
writer.SetInputConnection(dataImporter.GetOutputPort())
writer.Write()
