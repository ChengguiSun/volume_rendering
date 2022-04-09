from import_data import import_data
from filters import filters
import numpy as np
from realignment import realignment
from vol_pixel_filter import vol_pixel_filter

filename = "./Data/Code_and_Data_for_Students/Set1/Neutral1/T3-NA.mat"

Mocap,US_Stack = import_data(filename)

filter_tog = {"M":0,"C":1,"H":0,"Q":0,"V":1,"G":1}
filter_val = {"M":[1,1],"C":[0.6,0.8,0,1],"H":[1],"Q":[5,0.6],"G":[3]}

# Surface Augmentation and Verticut
for i in range(Mocap.shape[0]):
    US_Stack[:,:,i] = filters(US_Stack[:,:,i],filter_tog,filter_val)
    #print(np.amax(US_Stack[:,:,i]))

print(US_Stack.shape)

US_out = realignment(US_Stack,Mocap)

print(US_out.shape)

# rearrange/transpose array
US_t = np.transpose(US_out, (0,2,1))
print(US_t.shape)
# surface smoothing
filter_tog_ss = {"M":0,"C":0,"H":0,"Q":1,"V":0,"G":1} # ss for surface smoothing
filter_val_ss = {"M":[2,2],"C":[0.6,0.8,0,1],"H":[1],"Q":[5,0.8],"G":[2]}

for j in range(US_t.shape[2]):
    US_t[:,:,j] = filters(US_t[:,:,j],filter_tog_ss,filter_val_ss)
print(US_t.shape)

US = np.transpose(US_t, (0,2,1))

US=vol_pixel_filter(US, 20)
print(US.shape)
