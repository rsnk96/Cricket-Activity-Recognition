import os
import cv2
import sys
import glob
from subprocess import Popen
from pathlib import Path

ip_path = str(Path(sys.argv[1]))
if not os.path.isdir(ip_path):
    my_dir = os.path.splitext(ip_path)[0]
    os.makedirs(my_dir, exist_ok=True)
    call(f'ffmpeg -i {ip_path} {my_dir}/image-%04d.jpg')
    ip_path = my_dir

os.makedirs(ip_path+'_2dpoints', exist_ok=True)
openpose_cmd = str(Path('./openpose/bin/OpenPoseDemo.exe')) + f' --image_dir {ip_path} --write_json {ip_path}_2dpoints --write_images {ip_path}_2dpoints --display 0 --model_folder ' + str(Path('openpose/models'))  # --model_pose COCO
Popen(openpose_cmd).communicate()

## EDIT pose_keypoints_2d to pose_keypoints
files = glob.glob(str(Path(f'{ip_path}_2dpoints/*.json')))
for name in files:
    print(f'Fixing the 2d point json file {name} now')
    with open(name, 'r') as f:
        l = f.read().replace("pose_keypoints_2d","pose_keypoints")
    with open(name,'w') as f:
        f.write(l)
    keypoint_count=open(name,'r').read().count('\"pose_keypoints\"')
    if keypoint_count != 1:
        print(f'Deleting file {name} with {keypoint_count} poses detected')
        os.remove(name)


## makedirs png and gif_output
print('Running 3d pose regression now')
os.chdir('3d-pose-baseline')
os.makedirs('png',exist_ok=True)
os.makedirs('gif_output',exist_ok=True)

pose3d_cmd1 = 'python ' + str(Path('src/openpose_3dpose_sandbox.py'))+ ' --camera_frame --residual --batch_norm --dropout 0.5 --max_norm --evaluateActionWise --use_sh --epochs 200 --load 4874200 --openpose ' + str(Path(f'../{ip_path}_2dpoints')) + ' --write_gif'
Popen(pose3d_cmd1).communicate()

os.chdir('..')
