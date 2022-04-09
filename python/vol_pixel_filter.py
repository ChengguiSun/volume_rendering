import numpy as np
from skimage import measure
    
def vol_pixel_filter(Volume = None,TopNum = None): 
    
    #Check 3D connectivity
    CC = measure.label(Volume,26)
    numPixels = [np.size(PixelIdxList) for PixelIdxList in CC.PixelIdxList]
    Value = numPixels[::-1].sort()
    Index = numPixels[::-1].argsort()
    X,Y = numPixels.shape()
    start = TopNum
    end = None
    Index = Index[start:end]
    Index = np.sort(Index)
    for k in range(0,Y-TopNum):
        Volume[CC.PixelIdxList[Index[k]]] = 0
    
    return Volume