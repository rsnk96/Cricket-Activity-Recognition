import os
import cv2
import sys
import glob
from subprocess import call
from pathlib import Path

ip_path = str(Path(sys.argv[1]))
if not os.path.isdir(ip_path):
    my_dir = os.path.splitext(ip_path)[0]
    os.makedirs(my_dir, exist_ok=True)
    call(f'ffmpeg -i {ip_path} {my_dir}/image-%04d.jpg')
    ip_path = my_dir

os.makedirs(ip_path+'_2dpoints', exist_ok=True)
openpose_cmd = str(Path('./openpose/bin/OpenPoseDemo.exe')) + f' --image_dir {ip_path} --write_json {ip_path}_2dpoints --write_images {ip_path}_2dpoints --display 0 --model_folder ' + str(Path('openpose/models'))  # --model_pose COCO
call(openpose_cmd)

## EDIT pose_keypoints_2d to pose_keypoints
path = os.getcwd()+"\\temp_2dpoints"

files = glob.glob(f'{path}\*.json')
for name in files:
    with open(name, 'r') as f:
        l = f.read().replace("pose_keypoints_2d","pose_keypoints")
    with open(name,'w') as f:
        f.write(l)

## makedirs png and gif_output
os.chdir('3d-pose-baseline')
os.makedirs('png',exist_ok=True)
os.makedirs('gif_output',exist_ok=True)

pose3d_cmd1 = 'python ' + str(Path('src/openpose_3dpose_sandbox.py'))+ ' --camera_frame --residual --batch_norm --dropout 0.5 --max_norm --evaluateActionWise --use_sh --epochs 200 --load 4874200 --openpose ' + str(Path('../temp_2dpoints')) + ' --write_gif'
call(pose3d_cmd1)

os.chdir('..')