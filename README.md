# Cricket-Activity-Recognition
A repository for Cricket Activity Recognition

32 joints are saved out of which only 17 move. For more details, see [here](https://github.com/una-dinosauria/3d-pose-baseline/blob/1ca400232ad6158050d8b292ac812d94dbb49d74/src/data_utils.py#L20)

## To-Do
- [ ] Show that it can work on a much wider range of poses - include MSD's Helicopter for presentation
- [ ] 3D Pose mapping to reference frame
- [ ] Faster pose detection
- [ ] Do it for all players in a field
- [ ] Real-time requirements

## BUGS AND SOLUTIONS:
* If it comes checkpoint does not exist in Windows, it's because Windows has a maximum absolute length for the file name, and since the checkpoint folder is too deep in the folder, it doesn't recognize it
* NOTE: Switched off smoothing as it's having some corner cases where it doesn't work (first line in main of `openpose_3dpose_sandbox.py`)