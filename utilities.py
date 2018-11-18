#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 23:37:10 2018

@author: vivekkulkarni
"""
import cv2 
import os

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
