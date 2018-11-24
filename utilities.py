import os
import numpy as np
from glob import glob
from pathlib import Path
import matplotlib.pyplot as plt
import sys
sys.path.append(str(Path('3d-pose-baseline/src')))
import viz
import natsort
import imageio
import cv2
import imutils

standard_1 = str(Path('templates/pose_normalization/frame46.npy'))
standard_2 = str(Path('templates/pose_normalization/frame49.npy'))
standard_3 = str(Path('templates/pose_normalization/frame1.npy'))
standard_4 = str(Path('templates/pose_normalization/frame114.npy'))
standard_5 = str(Path('templates/pose_normalization/frame105.npy'))
standard_6 = str(Path('templates/pose_normalization/frame2.npy'))

s1 = np.load(standard_1)
s2 = np.load(standard_2)
s3 = np.load(standard_3)
s4 = np.load(standard_4)
s5 = np.load(standard_5)
s6 = np.load(standard_6)

s0 = (s1+s2+s3+s4+s5+s6)/6

def scale(a):
    shoulder_dist = 90.076*4
    lhip_dist = 76.46*4
    rhip_dist = 76.46*4
    lrhip_dist = 76.46*4
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
    path = Path(path)
    files = glob(str(path/'*.npy'))

        
    for name in files:
        t = np.load(name)
        if(i==0):       # for the first frame of the video alone
            t,ref = normalise(t,i,0)
            t = scale(t)
            i=i+1
        else:           # for the rest of the frames, since there is a reference now
            t,ref = normalise(t,i,ref)
            t = scale(t)

        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')
        viz.show3Dpose(t.flatten(),ax)
        plt.savefig(os.path.splitext(name)[0]+'.png')
        plt.close()
        os.remove(name)
        np.save(name,t)        # Overwrite the 3d pose with the normalized (rotation + scale) 3d pose

def find_occupancy_octant(pose):
    t, ref = normalise(pose,1, np.tile(pose[13],32).reshape(32,3))    # pose[13] is the thorax

    def assign_octant(point):
        if point[2]>0:
            if point[1]>0:
                if point[0]>0:
                    return 0
                else:
                    return 1
            else:
                if point[0]<=0:
                    return 2
                else:
                    return 3
        else:
            if point[1]>0:
                if point[0]>0:
                    return 4
                else:
                    return 5
            else:
                if point[0]<=0:
                    return 6
                else:
                    return 7

    # H36M_NAMES[17] = 'LShoulder'
    # H36M_NAMES[18] = 'LElbow'
    # H36M_NAMES[19] = 'LWrist'
    # H36M_NAMES[25] = 'RShoulder'
    # H36M_NAMES[26] = 'RElbow'
    # H36M_NAMES[27] = 'RWrist'

    r_wrist_octant = assign_octant(t[27])
    return r_wrist_octant


def generate_gif(images_path, resize=True):
    path = Path(images_path)
    files = natsort.natsorted(glob(str(path/'*.[pPjJ][nNpP][gGgG]')))
    imgs = []
    for name in files:
        img = cv2.cvtColor(cv2.imread(name), cv2.COLOR_BGR2RGB)
        if resize==True:
            img = imutils.resize(img, width=640)
        imgs.append(img)
    imageio.mimsave(str(path)+'.gif',imgs)