from import_data import import_data
from filters import filters
import numpy as np

filename = "F:/MM804/dataset/Code and Data for Students/Set 1/Neutral1/T3-NA.mat"

Mocap,US_Stack = import_data(filename)

filter_tog = {"M":0,"C":1,"H":0,"Q":0,"V":1,"G":1}
filter_val = {"M":[1,1],"C":[0.6,0.8,0,1],"H":[1],"Q":[5,0.6],"G":[3]}

for i in range(Mocap.shape[1]):
    US_Stack[:,:,i] = filters(US_Stack[:,:,i],filter_tog,filter_val)

