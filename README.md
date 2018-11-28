# Cricket-Activity-Recognition
A repository for Cricket Activity Recognition

32 joints are saved out of which only 17 move. For more details, see [here](https://github.com/una-dinosauria/3d-pose-baseline/blob/1ca400232ad6158050d8b292ac812d94dbb49d74/src/data_utils.py#L20)

## Execution procedures:
The implementation is strictly windows based and would require the command prompt.

-  Download OpenPose for windows machine from [here](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases/download/v1.4.0/openpose-1.4.0-win64-cpu-binaries.zip)

-  Unzip this in the parent folder `..\\Cricket-Activity-Recognition`

-  Open the command prompt in the parent folder `..\\Cricket-Activity-Recognition`

-  Run `python main.py "\\Cricket-Activity-Recognition\\folder\\to\\the_cricket_video"`



## To-Do
Presentation to-dos
- [X] Do it for all players in a field
- [ ] Show that it can work on a much wider range of poses - include MSD's Helicopter for presentation
- [X] Gif of cover drive
- [X] Talk about pose normalization and motion smooothing in ppt

Tech to-dos
- [X] One file to rule them all - main.py and the video file
- [X] Octant based tracking
- [X] Smoothen all gifs
- [x] Normalize pose (scale and orientation)
- [x] 3D Pose mapping to reference frame
- [ ] Faster pose detection?

## BUGS AND SOLUTIONS:
* If it comes checkpoint does not exist in Windows, it's because Windows has a maximum absolute length for the file name, and since the checkpoint folder is too deep in the folder, it doesn't recognize it
* NOTE: Switched off smoothing as it's having some corner cases where it doesn't work (first line in main of `openpose_3dpose_sandbox.py`)
