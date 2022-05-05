import argparse
from mat2mhd_sitk_singlefile import mat2mhd
from rendering_vtk_1win import render


parser = argparse.ArgumentParser(description='stand alone volume rendering app')

parser.add_argument('-p', "--path", type=str, required=True)

args = parser.parse_args()

output_name = mat2mhd(args.path)

render(output_name)