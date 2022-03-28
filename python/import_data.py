import numpy as np
import scipy.io as sio
from PIL import Image

def import_data(filename):

    mat_contents = sio.loadmat(filename)

    #print(mat_contents.keys())

    Mocap=mat_contents["Vertebra"]["MC"][0][0]

    MCShift = 1 #Frameshift Mocap Up 1 from calibration
    USShift = 2 #Frameshift U/S  Up 2 from calibration
    Res = 0.2 #Resolution, default at 0.2mm

    #print(Mocap.shape)

    Mocap_ave = np.copy(Mocap)

    # Mo-Cap 5-averaging and frameshift mocap
    Frames = Mocap.shape[0]

    for i in range(2,Frames-3):
        Mocap_ave[i,2:8] = np.mean(Mocap[i+MCShift-2:i+MCShift+3,2:8])

    Mocap[2:Frames-3,2:8]=Mocap_ave[2:Frames-3,2:8]

    new_mocap = None
    # Remove 0 frames from US
    for i in range(Frames):
        if Mocap[i,0] != 0:
            if new_mocap is None:
                new_mocap = [Mocap[i,:]]
            else:
                new_mocap = np.append(new_mocap, [Mocap[i,:]],axis=0)

    Mocap = new_mocap

    Frames = Mocap.shape[0]

    Mocap[:,2:9] = np.around(Mocap[:,2:9],decimals=1)
    Mocap[:,2:5]=Mocap[:,2:5]*10
    Mocap[:,2:5]=Mocap[:,2:5]/Res       #Round to 0.2mm but keep at real size
    Mocap[:,2:5]=np.around(Mocap[:,2:5])
    Mocap[:,2:5]=Mocap[:,2:5]*Res

    US_Stack = np.zeros((150,195,Frames-USShift),dtype=np.uint8)

    US = mat_contents["Vertebra"]["US"][0][0]


    for k in range(USShift,Frames):
        US =mat_contents["Vertebra"]["US"][0][0][:,:,k]
        US = US[60:417,90:552]
        new_US = np.asarray(Image.fromarray(US.astype('uint8')).resize((195,150)))
        US_Stack[:,:,k-USShift] = new_US


    Mocap = Mocap[:-USShift,]

    return Mocap,US_Stack

if __name__ == "__main__":
    filename = "F:/MM804/dataset/Code and Data for Students/Set 1/Neutral1/T3-NA.mat"

    Mocap,US_Stack = import_data(filename)

    print(Mocap.shape)
    print(US_Stack.shape)
    print(np.amax(US_Stack[:,:,1]))
    print(np.amin(US_Stack[:,:,1]))