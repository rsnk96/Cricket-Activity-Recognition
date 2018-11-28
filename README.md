# Cricket-Shot-Recognition
A repository for Cricket Activity Recognition

**NOTE**: This project will run very slow with just the CPU binaries of OpenPose. If you want it to run real time, compile it with GPU optimizations specific to your machine

## Setup procedure:

This is not needed if you are using the zip containing all the data in the right folders
- Install `ffmpeg`, `opencv-python`, `natsort`, `tensorflow`

- Clone this repository

-  Download OpenPose for windows machine from [here](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases/download/v1.4.0/openpose-1.4.0-win64-cpu-binaries.zip) and unzip this in the parent folder `Cricket-Activity-Recognition`

     Or, if you're on a linux machine, build it yourself from their [repository](https://github.com/CMU-Perceptual-Computing-Lab/openpose) and make sure the binaries are in the `<root of this repository>/openpose/bin` directory

- Download the `H3.6M` 3D embeddings by running the following commands from within the root of this repository
    ```bash
    cd 3d-pose-baseline
    mkdir data
    cd data
    wget https://www.dropbox.com/s/e35qv3n6zlkouki/h36m.zip
    unzip h36m.zip
    rm h36m.zip
    cd ..
    ```

- Place the pre-trained weights of the 2D to 3D pose estimation model, downloadable [here](https://drive.google.com/file/d/0BxWzojlLp259MF9qSFpiVjl0cU0/view?usp=sharing) and keep it inside the folder `3d-pose-baseline`

## Execution Guide
-  Open the command prompt in the parent folder `Cricket-Activity-Recognition`

-  Run `python main.py "location_to_video"`


Future Improvements
- [ ] Faster pose detection - replace OpenPose with PoseNet?
- [ ] Batter detection

## Bugs and Solutions
* If an error pops up saying `checkpoint does not exist` in Windows, it's because Windows has a maximum absolute length for the file name, and since the checkpoint folder is too deep in root folder, it doesn't recognize it

## Credits
This project hugely derives from [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) and [3d-pose-baseline](https://github.com/una-dinosauria/3d-pose-baseline) and applies a octant-occupancy based classification on top of the time-series of the joints' motion

## Authors
* R S Nikhil Krishna
* Vivek Kulkarni