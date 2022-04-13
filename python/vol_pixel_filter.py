import numpy as np
import cc3d
    
def vol_pixel_filter(Volume = None,TopNum = 20): 
    
    #Check 3D connectivity
    labels_out, N = cc3d.largest_k(Volume, k=TopNum, connectivity=26, delta=0, return_N=True)

    Volume = Volume * (labels_out > 0)
    print(N)
    
    return Volume