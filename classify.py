import os
import sys
import cv2
import utilities
import numpy as np
from glob import glob
from pathlib import Path
from scipy import stats

def assign_every_frame_octant(frames):
    test_data = [np.load(f) for f in frames]
    test_data_occupancy = [utilities.find_occupancy_octant(i) for i in test_data]
    if len(test_data_occupancy)==0:
        print('Sorry, insufficient data to test, possible reason: this code only works if there is only one person in the frame right now')
        return

    mod = stats.mode(test_data_occupancy)[0]
    occ = 1.0*test_data_occupancy.count(mod) / len(test_data_occupancy)
    uniq,uniq_wo_noise = [],[]
    for ele in test_data_occupancy:
        if ele not in uniq:
            uniq+=[ele]
    # Noise removal
    for ele in uniq:
        if 1.0*test_data_occupancy.count(ele) / len(test_data_occupancy) > 0.1:
            uniq_wo_noise += [ele]

    def contains(small, big):
        for i in range(len(big)-len(small)+1):
            for j in range(len(small)):
                if big[i+j] != small[j]:
                    break
            else:
                return i, i+len(small)
        return False
       
    print(f'Mode:{mod}, Fraction occupance:{occ}, Unique elements:{uniq}')
    
    shot_type='Pull'
    if occ>0.5 and mod==5 and (6 not in test_data_occupancy or 7 not in test_data_occupancy):
        shot_type = 'Cover'
        print(f'It\'s a {shot_type} shot!!!')
        return
    elif contains([5,7,4], uniq) or contains([5,6,7],uniq) or contains([5,1,7], uniq):
        shot_type='Sweep'
        print(f'It\'s a {shot_type} shot!!!')
        return
    elif 7 not in uniq_wo_noise and 1 not in uniq_wo_noise:
        shot_type = 'Cut'
        print(f'It\'s a {shot_type} shot!!!')
        return
    else:
        print(f'It\'s a {shot_type} shot!!!')
        return


folders = glob(str(Path('dataset/*_3dpoints/')))

if len(sys.argv)>1:
    assign_every_frame_octant(glob(str(Path(sys.argv[1])/'*.npy')))
else:
    for f in folders:
        print('Folder: ',f, end='\t')
        assign_every_frame_octant(glob(str(Path(f)/'*.npy')))