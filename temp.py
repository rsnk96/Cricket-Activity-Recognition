import numpy as np
import os 
import glob
import viz
import matplotlib.pyplot as plt

path_cut8 = 'cut_8'
path_cut4 = 'cut_4'
path_cut1 = 'cut_1'

path_cover1 = 'cover_1'
path_cover2 = 'cover_2'
path_cover3 = 'cover_3'
path_cover4 = 'cover_4'
path_cover5 = 'cover_5'

names_1 = sorted(glob.glob((os.path.join(path_cut1,'*.npy'))))
names_4 = glob.glob((os.path.join(path_cut4,'*.npy')))
names_8 = glob.glob((os.path.join(path_cut8,'*.npy')))

names1 = glob.glob((os.path.join(path_cover1,'*.npy')))
names2 = glob.glob((os.path.join(path_cover2,'*.npy')))
names3 = glob.glob((os.path.join(path_cover3,'*.npy')))
names4 = glob.glob((os.path.join(path_cover4,'*.npy')))
names5 = glob.glob((os.path.join(path_cover5,'*.npy')))

cut_8 = []
for name in names_8:
    d = np.load(name)
    cut_8.append(d)
    
cut_4 = []    
for name in names_4:
    d = np.load(name)
    cut_4.append(d)

cut_1 = []
for name in names_1:
    d = np.load(name)
    cut_1.append(d)    
    
d8 = cut_8[0]
d4 = cut_4[0]
d1 = cut_1[0]    

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose(d8.flatten(),ax)

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose(d1.flatten(),ax)

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose(d4.flatten(),ax)

t = d8 - d4
t1 = d8 - d1
t3 = d1 - d4
#t2 = (t+t1+t3)/3
t2 = (t+t1)/2

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose((d8-t1).flatten(),ax)

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose((d4-t3).flatten(),ax)

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose((d4-t3).flatten(),ax)

cover1 = []
cover2 = []
cover3 = []
cover4 = []
cover5 = []

for name in names1:
    e = np.load(name)
    cover1.append(e)
    
for name in names2:
    e = np.load(name)
    cover2.append(e)
    
for name in names3:
    e = np.load(name)
    cover3.append(e) 
    
for name in names4:
    e = np.load(name)
    cover4.append(e)    
 
for name in names5:
    e = np.load(name)
    cover5.append(e)

e1 = cover1[0]
e2 = cover2[0]
e3 = cover3[0]
e4 = cover4[0]
e5 = cover5[54]

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose(e1.flatten(),ax)

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose(e2.flatten(),ax)

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose(e3.flatten(),ax)

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose(e4.flatten(),ax)

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose(e5.flatten(),ax)
    

s1 = e1-e5
s2 = e2-e5
s3 = e3 - e5
s4 = e4 - e5

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose((e1-s1).flatten(),ax)

eet = cover5[43]
s5 = eet-e5

#etest = cover5[0]
#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose((etest).flatten(),ax)

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose((e5).flatten(),ax)

#fig=plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#viz.show3Dpose((etest-s5).flatten(),ax)


k=[10,2,7,6]

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
viz.show3Dpose((e4-s4).flatten(),ax)


for i in k:
    e6 = cover4[i]
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    viz.show3Dpose((e6-s4).flatten(),ax)
