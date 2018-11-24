#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 02:58:51 2018

@author: vivekkulkarni
"""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.model_selection import GridSearchCV as gsc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
#from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
#from sklearn.metrics import confusion_matrix

def make_data(X,y):
    onehotencoder= OneHotEncoder(categorical_features= [0])
    y = onehotencoder.fit_transform(y.reshape(-1,1)).toarray()
    X = [np.array(list(map(lambda x: x.flatten(), temp))) for temp in X]
    X = np.array(list(map(lambda x: x.flatten(), X)))
    return X,y

def with_knn(X,y,si):
    X,y = make_data(X,y)
    Xtrain,Xtest, ytrain, ytest = train_test_split(X,y,test_size=si,random_state=0)
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(Xtrain,ytrain)
    predicts = model.predict(Xtest)
    return ytest,predicts

def with_svm(X,y,si):
    X,y = make_data(X,y)
    Xtrain,Xtest, ytrain, ytest = train_test_split(X,y,test_size=si,random_state=0)
    model = SVC(gamma='scale')
    model.fit(Xtrain,ytrain[:,0])
    predicts = model.predict(Xtest)
    return ytest,predicts