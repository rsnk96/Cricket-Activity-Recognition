import os
import numpy as np
from glob import glob

standard_1 = 'points/cover_5/frame46.npy'
standard_2 = 'points/cut_1/frame49.npy'
standard_3 = 'points/cut_4/frame1.npy'
standard_4 = 'points/edit_1/frame114.npy'
standard_5 = 'points/edit_2/frame105.npy'
standard_6 = 'points/sweep_2/frame2.npy'

s1 = np.load(standard_1)
s2 = np.load(standard_2)
s3 = np.load(standard_3)
s4 = np.load(standard_4)
s5 = np.load(standard_5)
s6 = np.load(standard_6)

s0 = (s1+s2+s3+s4+s5+s6)/6

def scale(a):
    shoulder_dist = 90.076
    lhip_dist = 76.46
    rhip_dist = 76.46
    lrhip_dist = 76.46
    k1 = a
    sd = np.sqrt(np.sum((k1[1,:] - k1[25,:])**2))
    lhd = np.sqrt(np.sum((k1[6,:] - k1[0,:])**2))
    rhd = np.sqrt(np.sum((k1[1,:] - k1[0,:])**2))
    lrhd = np.sqrt(np.sum((k1[1,:] - k1[0,:])**2))
    sr = sd/shoulder_dist
    lr = lhd/lhip_dist
    rr = rhd/rhip_dist
    lrr = lrhd/lrhip_dist
    rt = (sr+lr+rr+lrr)/4
    k1 = k1/rt
    return k1
    
def normalise(a,i,ref):
    ref1 = ref
    if(i==0):
        ref1 = a-s0
    t = a-ref1    
    return t,ref1            

def make_3dpoints(path):
    i = 0
    files = glob(os.path.join(path,'*.npy'))
    for name in files:
        t = np.load(name)
        if(i==0):
            t,ref = normalise(t,i,0)
            t = scale(t)
            i=i+1
        else:
            t,ref = normalise(t,i,ref)
            t = scale(t)
        np.save(path+'/'+name,t)        