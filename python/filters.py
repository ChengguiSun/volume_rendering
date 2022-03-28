import cv2
import numpy as np
import scipy.signal as signal

def filters(US,tog,val):

    if tog["H"] == 1:
        #top hat filter
        filterSize =(3, 3)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, 
                                   filterSize)
        US = cv2.morphologyEx(US, 
                              cv2.MORPH_TOPHAT,
                              kernel)
    if tog["G"] == 1:
        #averaging
        kernel = np.ones((val["G"][0],val["G"][0]))/(val["G"][0]*val["G"][0])
        US = signal.correlate2d(US,kernel,"same")
    
    if tog["M"] == 1:
        #median filter
        US = signal.medfilt(US,(3,3))
    
    if tog["C"] == 1:
        #contrast filter
        vin_low = int(val["C"][0]*255)
        vin_up = int(val["C"][1]*255)
        vout_low = int(val["C"][2]*255)
        vout_up = int(val["C"][3]*255)
        scale = (vin_up - vin_low) / (vout_up - vout_low)
        for r in range(US.shape[0]):
            for c in range(US.shape[1]):
                vs = max(US[r,c] - vin_low, 0)
                vd = min(int(vs * scale + 0.5) + val["C"][2], val["C"][3])
                US[r,c] = vd
    if np.amax(US) < 15:
        US = np.zeros(US.shape,dtype=np.uint8)

    if tog["Q"] == 1:
        #otsu thresholding
        US,thresh = cv2.threshold(US,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    return US
    
    
