import vtk

fileName = "../output/T3-NA.mhd" # path to the MHA file
reader = vtk.vtkMetaImageReader()
reader.SetFileName(fileName)
reader.Update()

## Set the output for viewpoint1
# Create colour transfer function
colorFunc = vtk.vtkColorTransferFunction()
colorFunc.AddRGBPoint(0, 0.0, 0.0, 0.0) # extracted values with 3D slicer
colorFunc.AddRGBPoint(20, 0.168627, 0.0, 0.0) # 43, 0, 0
colorFunc.AddRGBPoint(40, 0.403921, 0.145098, 0.078431) # 103, 37, 20
colorFunc.AddRGBPoint(120, 0.780392, 0.607843, 0.380392) # 199, 155, 97
colorFunc.AddRGBPoint(220, 0.847059, 0.835294, 0.788235) # 216, 213, 201
colorFunc.AddRGBPoint(1024, 1, 1, 1) # 255, 255, 255

# Create opacity transfer function
alphaChannelFunc = vtk.vtkPiecewiseFunction() # extracted values with 3D slicer
alphaChannelFunc.AddPoint(0, 0.0)
alphaChannelFunc.AddPoint(20, 0.0)
alphaChannelFunc.AddPoint(100.08, 0.06)
alphaChannelFunc.AddPoint(335.05, 0.33)
alphaChannelFunc.AddPoint(590.32, 0.49)
alphaChannelFunc.AddPoint(1024, 0.50)

# Instantiate necessary classes and create VTK pipeline
volume = vtk.vtkVolume()
volumeMapper = vtk.vtkSmartVolumeMapper()  # Define volume mapper
volumeMapper.SetInputConnection(reader.GetOutputPort())
volumeProperty = vtk.vtkVolumeProperty() # Define volume properties
volumeProperty.SetScalarOpacity(alphaChannelFunc)
volumeProperty.SetColor(colorFunc)
volumeProperty.ShadeOn()
volume.SetMapper(volumeMapper) # Set the mapper and volume properties
volume.SetProperty(volumeProperty)


## Set the output for viewpoint2
# Apply matching cubes algorithm
iso = vtk.vtkMarchingCubes()
iso.SetInputConnection(reader.GetOutputPort())
iso.ComputeGradientsOn()
iso.ComputeScalarsOff()
iso.SetValue(0, 100)

# Polydata mapper for the iso-surface
isoMapper = vtk.vtkPolyDataMapper()
isoMapper.SetInputConnection(iso.GetOutputPort())
isoMapper.ScalarVisibilityOff()

# Actor for the isosurface
isoActor = vtk.vtkActor()
isoActor.SetMapper(isoMapper)
isoActor.GetProperty().SetColor(0.5,0.5,0.5)


## Set the viewports 
# Viewport 1
ren1 = vtk.vtkRenderer()
ren1.SetViewport(0.0, 0.0, 0.33, 1.0)
ren1.AddVolume(volume) # Add the volume to the renderer

# Viewport 2
ren2 = vtk.vtkRenderer()
ren2.SetViewport(0.33, 0.0, 0.67, 1.0)
ren2.AddActor(isoActor) # Add the volume to the renderer

# Viewport 3
ren3 = vtk.vtkRenderer()
ren3.SetViewport(0.67, 0, 1.0, 1.0)
ren3.AddActor(isoActor) # combine isosurface
ren3.AddVolume(volume) # with volume

renWin = vtk.vtkRenderWindow()
# colors = vtk.vtkNamedColors() # set viewports color
# ren1.SetBackground(colors.GetColor3d("silver"))
# ren2.SetBackground(colors.GetColor3d("silver"))
# ren3.SetBackground(colors.GetColor3d("silver"))
renWin.SetSize(1200, 400)

renWin.AddRenderer(ren1)
renWin.AddRenderer(ren2)
renWin.AddRenderer(ren3)
# renWin.Render()

# Set renderer window
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

cam1 = vtk.vtkCamera()
cam1 = ren1.GetActiveCamera()
cam1.SetPosition(4.9202, -2.10678, 3.30955)
cam1.SetFocalPoint(0.0, 0.0, 0.0)
cam1.SetClippingRange(0.312589, 312.589)
cam1.SetViewUp(0.60866, 0.592511, -0.527696)
ren1.SetActiveCamera(cam1)
ren2.SetActiveCamera(cam1)
ren2.ResetCamera() # reset camera to show objects
ren3.SetActiveCamera(cam1)
ren3.ResetCamera() # reset camera to show objects

# Render the scene
iren.Initialize()
renWin.Render()
iren.Start()

# print(reader.GetOutput())
print("Dataset dimension: ",reader.GetOutput().GetDimensions())
print("Dataset voxel resolution: ",reader.GetOutput().GetSpacing()) 
print("Pixel intensities: ",reader.GetOutput().GetScalarRange())
