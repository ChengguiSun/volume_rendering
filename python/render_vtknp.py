"""
Render volume with vtk and numpy from an array.
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
# dataImporter.SetDataSpacing(1, 1, 1)
dataImporter.SetWholeExtent(0, 479, 0, 639, 0, 1199)
# dataImporter.update()

alphaChannelFunc = vtk.vtkPiecewiseFunction() # store transparency-values
# alphaChannelFunc.AddPoint(0, 0.0)
# alphaChannelFunc.AddPoint(50, 0.05)
# alphaChannelFunc.AddPoint(100, 0.1)
# alphaChannelFunc.AddPoint(150, 0.2)
# alphaChannelFunc.AddPoint(255, 0.3)
alphaChannelFunc.AddPoint(0, 0.0)
alphaChannelFunc.AddPoint(80, 0.0)
alphaChannelFunc.AddPoint(100, 0.1)
alphaChannelFunc.AddPoint(250, 0.2)

colors = vtk.vtkNamedColors() # stores color data
colorFunc = vtk.vtkColorTransferFunction()
colorFunc.AddRGBPoint(50, 1.0, 0.0, 0.0)
colorFunc.AddRGBPoint(100, 0.0, 1.0, 0.0)
colorFunc.AddRGBPoint(150, 0.0, 0.0, 1.0)

volumeProperty = vtk.vtkVolumeProperty() # add properties to volume
volumeProperty.SetColor(colorFunc)
volumeProperty.SetScalarOpacity(alphaChannelFunc)
# volumeProperty.SetInterpolationTypeToLinear()

volumeMapper = vtk.vtkFixedPointVolumeRayCastMapper()
volumeMapper.SetInputConnection(dataImporter.GetOutputPort())

volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

# initialize the renderer and window
renderer = vtk.vtkRenderer()
renderWin = vtk.vtkRenderWindow()
renderWin.AddRenderer(renderer)
renderInteractor = vtk.vtkRenderWindowInteractor()
renderInteractor.SetRenderWindow(renderWin)

# add the volume to the renderer ...
renderer.AddVolume(volume)
renderer.SetBackground(colors.GetColor3d("MistyRose"))

renderWin.SetSize(400, 400)
renderWin.SetWindowName('VTKWithNumpy')

renderInteractor.Initialize()

renderWin.Render()
renderInteractor.Start()

print(len(data_string))
