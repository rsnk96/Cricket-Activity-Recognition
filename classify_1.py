#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:54:56 2018

@author: vivekkulkarni
"""
import numpy as np
import utilities
import processing

directry = '/home/vivekkulkarni/Cricket-Activity-Recognition/image_translated/points'
X,y = utilities.get_train_test(directry)
y = np.array(y)

ytest,ytrue = processing.with_svm(X,y,0.25)
ytest,ytrue = processing.with_knn(X,y,0.25)