from matplotlib.pyplot import axis
import numpy as np

def Transformer(rx,ry,rz,tx,ty,tz):
    translation = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[tx,ty,tz,1]])
    xrot = np.array([[1,0,0,0],[0,np.cos(np.radians(rx)),np.sin(np.radians(rx)),0],[0,-np.sin(np.radians(rx)),np.cos(np.radians(rx)),0],[0,0,0,1]])
    yrot = np.array([[np.cos(np.radians(ry)),0,-np.sin(np.radians(ry)),0],[0,1,0,0],[np.sin(np.radians(ry)),0,np.cos(np.radians(ry)),0],[0,0,0,1]])
    zrot = np.array([[np.cos(np.radians(rz)),np.sin(np.radians(rz)),0,0],[-np.sin(np.radians(rz)),np.cos(np.radians(rz)),0,0],[0,0,1,0],[0,0,0,1]])

    return zrot @ yrot @ xrot @ translation

def Vol_Sizing(list):
    #Adjust coordinates into Postive integer dimensions.
    maxmin = np.zeros((3,3))
    for i in range(3):
        maxmin[i,0] = np.amin(list[:,i])
        maxmin[i,1] = np.amax(list[:,i])
        maxmin[i,2] = 1 + maxmin[i,1] - maxmin[i,0]
        list[:,i] = 1 + list[:,i] - maxmin[i,0]
    dim_min = [maxmin[0,0],maxmin[1,0],maxmin[2,0]]
    dim_max = [maxmin[0,1],maxmin[1,1],maxmin[2,1]]

    return maxmin,dim_min,dim_max,list

def realignment(US,MC):
    frames = MC.shape[0]
    MC[:,2:5] = MC[:,2:5]/2
    pixel_value = []

    for j in range(frames):
        if np.sum(US[:,:,j]) == 0:
            continue
        #Obtain coordinates of non-zero values
        #print(US[:,:,j].shape)
        ax_pos, lat_pos = np.nonzero(US[:,:,j])
        #print(len(ax_pos))
        val = np.zeros((len(ax_pos),1))
        #Obtain values at each of these coordinates
        for k in range(len(ax_pos)):
            val[k,0] = US[ax_pos[k],lat_pos[k],j]
        ax_pos = np.array([ax_pos]).T
        lat_pos = np.array([lat_pos]).T
        ax_pos = ax_pos - 1
        lat_pos = lat_pos - 1
        #All ultrasound frame values converted into vector form
        F_size = ax_pos.shape[0]
        Frame_pose = np.zeros((F_size,1))
        Quat_pose = np.ones((F_size,1))
        R_vector = np.concatenate([lat_pos,ax_pos,Frame_pose,Quat_pose],axis=1)

        #print(R_vector.shape)
        #Load motion capture data into transformer
        lat_r = -MC[j,5]
        ax_r = MC[j,6]
        fr_r = -MC[j,7]
        lat = -MC[j,2]
        ax = -MC[j,3]
        fr = MC[j,4]

        transform = Transformer(lat_r,ax_r,fr_r,lat,ax,fr)

        R_new = R_vector @ transform
        R_new = np.concatenate([R_new,val],axis=1)
        if len(pixel_value) == 0:
            pixel_value = R_new
        else:
            pixel_value = np.concatenate([pixel_value,R_new],axis=0)

    pixel_value = np.round(pixel_value,0)
    pixel = np.unique(pixel_value,axis=0)
    
    MM,dim_min,dim_max,pixel = Vol_Sizing(pixel)

    #print(MM)

    N_pixel = pixel.shape[0]
    US_out = np.zeros((int(MM[1,2])+1,int(MM[0,2])+1,int(MM[2,2])+1),dtype=np.uint16)
    
    for k in range(N_pixel):
        US_out[int(pixel[k,1]),int(pixel[k,0]),int(pixel[k,2])] = int(pixel[k,4])
    
    return US_out
