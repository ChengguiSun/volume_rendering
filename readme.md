This file is created for MM804 project. Please create your branch to write codes for this project.

# Accredit
Some of the scripts are written based on course lectures.

# Installation
All commands listed here are sample commands and written based on Windows OS. To run the scripts on other OS, please change the commands accordingly.

# Prerequisites
* Python 3.8
* vtk == 9.1.0

# Setup Python environment and install vtk
*	setup python virtual environment: python3.8 -m venv env
*	activate virtual environment: env/Scripts/activate
*	install vtk: pip install -r requirements.txt
*	run a specific script python python/filename.py

# About folders and files
* **python** folder has the following python scripts;
  * *mat2mhd_sitk_singlefile.py:* convert a single .mat file to .mhd file using SimpleITK **(recommended)**;
  * *mat2mhd_sitk_batchfiles.py:* convert .mat files in one folder to .mhd files using SimpeITK **(recommended)**;
  * *mat2mhd_vtk.py:* convert a single .mat file to .mhd file using VTK (need to be improved and not recommended);
  * *volume_rendering.py:* perform volume rendering from .mhd file/files using VTK. The opacity and color values need to be set with the help of 3D Slicer **(recommended)**;
  * *render_vista.py:* perform volume rendering from .mat file/files using pyvista (need to be improved and not recommended);
  * *render_vtknp.py:* perform volume rendering from .mat file/files using numpy and VTK (need to be improved and not recommended);
  * *matscanner.py:* read keys of from .mat file/files.

* matlab folder has matlab scripts for image pre-processing;
* output has sample results of volume rendering.
