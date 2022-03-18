"""Render np.array volume with vtk and numpy."""

import numpy as np
import scipy.io
import vtkmodules.vtkInteractionStyle
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPiecewiseFunction
from vtkmodules.vtkIOImage import vtkImageImport
from vtkmodules.vtkRenderingCore import (
    vtkColorTransferFunction,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkVolume,
    vtkVolumeProperty
)
from vtkmodules.vtkRenderingVolume import vtkFixedPointVolumeRayCastMapper
from vtkmodules.vtkRenderingVolumeOpenGL2 import vtkOpenGLRayCastImageDisplayHelper

# import data from mat file
mat = scipy.io.loadmat('./Data/Code_and_Data_for_Students/Set1/Neutral1/T10-NA.mat')
arr = mat['Vertebra'][0,0][1]
data_arr = arr.astype(np.uint8)  

# imports raw data and stores it.
dataImporter = vtkImageImport()
data_string = data_arr.tobytes() # array is converted to a string of chars and imported.
dataImporter.CopyImportVoidPointer(data_string, len(data_string))
dataImporter.SetDataScalarTypeToUnsignedChar() # data set to unsigned char (uint8)
dataImporter.SetNumberOfScalarComponents(1) 
dataImporter.SetDataExtent(0, 479, 0, 639, 0, 1199) # 3d dimension
dataImporter.SetWholeExtent(0, 479, 0, 639, 0, 1199)

alphaChannelFunc = vtkPiecewiseFunction() # store transparency-values
alphaChannelFunc.AddPoint(0, 0.0)
alphaChannelFunc.AddPoint(50, 0.05)
alphaChannelFunc.AddPoint(100, 0.1)
alphaChannelFunc.AddPoint(150, 0.2)

colors = vtkNamedColors() # stores color data
colorFunc = vtkColorTransferFunction()
colorFunc.AddRGBPoint(50, 1.0, 0.0, 0.0)
colorFunc.AddRGBPoint(100, 0.0, 1.0, 0.0)
colorFunc.AddRGBPoint(150, 0.0, 0.0, 1.0)

volumeProperty = vtkVolumeProperty() # add properties to volume
volumeProperty.SetColor(colorFunc)
volumeProperty.SetScalarOpacity(alphaChannelFunc)

volumeMapper = vtkFixedPointVolumeRayCastMapper()
volumeMapper.SetInputConnection(dataImporter.GetOutputPort())

volume = vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

# initialize the renderer and window
renderer = vtkRenderer()
renderWin = vtkRenderWindow()
renderWin.AddRenderer(renderer)
renderInteractor = vtkRenderWindowInteractor()
renderInteractor.SetRenderWindow(renderWin)

# add the volume to the renderer ...
renderer.AddVolume(volume)
renderer.SetBackground(colors.GetColor3d("MistyRose"))

renderWin.SetSize(400, 400)
renderWin.SetWindowName('VTKWithNumpy')

renderInteractor.Initialize()

renderWin.Render()
renderInteractor.Start()
