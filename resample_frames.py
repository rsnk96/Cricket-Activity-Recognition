import os
import sys
from glob import glob
from random import sample
from pathlib import Path
from natsort import natsorted

NUMBER_OF_FRAMES_DESIRED = 40

frames = natsorted(glob(f'{sys.argv[1]}/*'))
chosen_ones = frames[::len(frames)//NUMBER_OF_FRAMES_DESIRED]
chosen_ones = [chosen_ones[i] for i in sample(range(len(chosen_ones)), NUMBER_OF_FRAMES_DESIRED)]       # To remove remainder

print(len(frames), len(chosen_ones), len(frames), NUMBER_OF_FRAMES_DESIRED)

for frame in frames:
    if frame not in chosen_ones:
        print(f'Kick {frame}')
        os.remove(frame)
