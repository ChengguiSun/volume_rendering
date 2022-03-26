"""
Write .mat file to MetaImage using vtk and numpy.
The .mhd files created by this method don't work very well with 3D slicer. 
"""

import numpy as np
import scipy.io
import vtk

# import data from mat file
mat = scipy.io.loadmat('./Data/Code_and_Data_for_Students/Set1/Neutral1/T10-NA.mat')
arr = mat['Vertebra'][0,0][1]
data_arr = arr.astype(np.uint8)  # uint8 max value 255

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
