#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:56:30 2018

@author: vivekkulkarni
"""

import os
import natsort
import imageio
import cv2 
path = '/home/vivekkulkarni/Cricket-Activity-Recognition/image_translated/points'

for root, dirs, files in os.walk(path):
    f = natsort.natsorted(files)
    files = [ fi for fi in f if not (fi.endswith(".json") or fi.endswith(".gif"))]
    img = []
    for name in files:
        ptr = root+'/'+name
        k = cv2.imread(ptr)
        img.append(k)
    if root is not path: 
        imageio.mimsave(root+'.gif',img)