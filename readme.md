This repo is created for MM project - Reconstruction and Visualization of 3D
Anatomical Structures Using a Sequence of 2D Ultrasound Images. Please create 
your branch to write codes for this project.

# Accredit
Some of the scripts are written based on course lectures.

# Installation
All commands listed here are sample commands and written based on Windows OS. 
To run the scripts on other OS, please change the commands accordingly.

# Prerequisites
* Python 3.8
* vtk == 9.1.0

# Setup Python environment and install vtk
*	setup python virtual environment: python3.8 -m venv env
*	activate virtual environment: env/Scripts/activate
*	install vtk: pip install -r requirements.txt (Conflicts between packages may 
occur when using this command to install packages. Please solve the conflicts
manually according to the exact errors)  
*	run a specific script with this command: python python/filename.py
* run stand_alone.py followed by .mat file path to directly get the result 
```
python stand_alone.py -p "your_mat_path"
```

# About folders and files
* **python** folder has the following python scripts;
  * *import_data.py*: import data from .mat file；
  * *filters.py*: remove noise and artifacts, and augment surface；
  * *realignment.py*: realignment US image frames；
  * *vol_pixel_filter.py*: smooth 3D volume surface；
  * *import_and_filt.py*: import data and perform filtering；
  * *import_and_preprocess.py*: import data and perform surface augmentation, realignment, and surface smoothing all at once **(recommended)**；
  * *mat2mhd_sitk_singlefile.py*: convert a single .mat file to .mhd file using SimpleITK **(recommended)**;
  * *mat2mhd_sitk_batchfiles.py*: convert .mat files in one folder to .mhd files using SimpeITK **(recommended)**;
  * *rendering_vtk_1win.py*: display visualization results with VTK using volume and surface rendering in one viewport **(recommended)**;
  * *rendering_vtk_3win.py*: display volume rendering, surface rendering and volume and surface combined rendering results with VTK with three viewports **(recommended)**;
  * *render_vista.py*: perform reconstruction and volume rendering from .mat file/files using PyVista **(recommended)**;
  * *render_vtknp.py*: perform volume rendering from .mat file/files using Numpy and VTK (need to be improved and not recommended);
  * *mat2mhd_vtk.py*: convert a single .mat file to .mhd file using VTK (need to be improved and not recommended);
  * *matscanner.py*: Print the keys of a .mat file and get the dimension of arrays.

* output has sample results of volume rendering.
