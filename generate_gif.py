import os
import natsort
import imageio
import cv2 
import sys
import imutils
from pathlib import Path
from glob import glob

if not sys.argv[1]:
    paths = ['cover_1_2dpoints', 'cover_2_2dpoints', 'cover_4_2dpoints', 'cover_3_2dpoints', 'cover_4_2dpoints', 'cover_5_2dpoints', 'cover_6_2dpoints', 'Cut_1_2dpoints','Cut_4_2dpoints','Cut_8_2dpoints', 'edit_1_2dpoints', 'edit_2_2dpoints', 'edit_4_2dpoints', 'edit_3_2dpoints', 'edit_5_2dpoints', 'Sweep_1_Medium_2dpoints', 'Sweep_2_Medium_2dpoints']
else:
    paths = [sys.argv[1]]

# path = Path(sys.argv[1])

for p in paths:
    path = Path(p)
    files = natsort.natsorted(glob(str(path/'*.[pPjJ][nNpP][gGgG]')))
    img = []
    for name in files:
        temp = cv2.cvtColor(cv2.imread(name), cv2.COLOR_BGR2RGB)
        k = imutils.resize(temp, width=640)
        img.append(k)
    imageio.mimsave(str(path)+'.gif',img)