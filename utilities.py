#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 23:37:10 2018

@author: vivekkulkarni
"""
import cv2 
import os
import numpy as np
from natsort import natsorted
import random

def make_the_images(path):
    for root, dirs, files in os.walk(path):  
        for filename in files:
           name=os.path.splitext(filename)[0]
           name = path+'/'+name
           f = path+'/'+filename
           print(name)
           if not (os.path.isdir(name) or ('frame' in name)):
               os.mkdir(name)
           vidcap = cv2.VideoCapture(f)
           success,image = vidcap.read()
           count = 0
           while success:
               name1 = name+'/'+'frame'+str(count)+'.jpg'
               cv2.imwrite(name1, image)     # save frame as JPEG file      
               success,image = vidcap.read()
               count += 1 

def get_train_test(directry):
#    directry = '/home/vivekkulkarni/Cricket-Activity-Recognition/image_translated/points'    
    di = []
    nn = []    
    for root,dirs,files in os.walk(directry):
        f = natsorted(files)
        files = [ fi for fi in f if not (fi.endswith(".png") or fi.endswith(".gif"))]
        di.append(root)
        dk = []
        for name in files:
            t = root+'/'+name
            dk.append(np.load(t))
        nn.append(dk)
    nn.pop(0)
    di.pop(0)
        
    NUMBER_OF_FRAMES_DESIRED = min([len(i) for i in nn])    
    ll = []
    y = []
    for i in range(len(nn)):
        frames = nn[i]
        chosen_ones = frames[::len(frames)//NUMBER_OF_FRAMES_DESIRED]
        chosen_ones = [chosen_ones[i] for i in random.sample   (range(len(chosen_ones)), NUMBER_OF_FRAMES_DESIRED)]       # To remove remainder
        ll.append(chosen_ones)
        l = os.path.split(di[i])[1]
        if('cut' in l):
            y.append(0)
        elif('cover' in l):
            y.append(1)
        elif('sweep' in l):
            y.append(2)
        else:
            y.append(3)
    return ll,y
            