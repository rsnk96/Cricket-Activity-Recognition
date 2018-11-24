#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:36:04 2018

@author: vivekkulkarni
"""
import numpy as np
import os 
import natsort
import sys
from pathlib import Path
sys.path.append(str(Path('3d-pose-baseline/src')))
import viz
import matplotlib.pyplot as plt

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

#check a similarity metric for gauging the solution for the ones where we don't need to move
plt.ioff()
path = 'points'
directry = '/home/vivekkulkarni/Cricket-Activity-Recognition/image_translated'
dirr = []
dat = []
for root,dirs,files in os.walk(path):
    f = natsort.natsorted(files)
    files = [ fi for fi in f if not (fi.endswith(".json") or fi.endswith(".gif"))]
    i = 0
    na = directry + '/' + root
    os.makedirs(na,exist_ok = True)
    img = []
    for name in files:
        t = root+'/'+name
        dirr.append(t)
        if(i==0):
            x = np.load(t)
            x_ref = x - s0
            xtemp = x-x_ref
        else:
            x = np.load(t)
            xtemp = x-x_ref
        i=i+1
        dat.append(xtemp)
        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')
        viz.show3Dpose(xtemp.flatten(),ax)
        nn = directry + '/'+t
        nn = os.path.splitext(nn)[0]
#        nn1 = nn+'.png'
#        plt.savefig(nn1) 
        np.save(nn+'.npy',xtemp)