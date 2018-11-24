import os
import sys
import cv2
import utilities
import numpy as np
from glob import glob
from pathlib import Path
from sklearn.neighbors import NearestNeighbors

cover_templates = Path('templates/cover')
cut_templates = Path('templates/cut')
pull_templates = Path('templates/pull')
sweep_templates = Path('templates/sweep')

template_poses_cover = [np.load(f).flatten() for f in glob(str(cover_templates/'*.npy'))]
template_poses_cut = [np.load(f).flatten() for f in glob(str(cut_templates/'*.npy'))]
template_poses_pull = [np.load(f).flatten() for f in glob(str(pull_templates/'*.npy'))]
template_poses_sweep = [np.load(f).flatten() for f in glob(str(sweep_templates/'*.npy'))]


def direct_search_for_poses():
    test_data = np.array([np.load(f).flatten() for f in glob(str(Path(sys.argv[1])/'*.npy'))])
    test_nn = NearestNeighbors(n_neighbors=1).fit(test_data)

    cover_distances = test_nn.kneighbors(np.array(template_poses_cover))
    cut_distances = test_nn.kneighbors(np.array(template_poses_cut))
    pull_distances = test_nn.kneighbors(np.array(template_poses_pull))
    sweep_distances = test_nn.kneighbors(np.array(template_poses_sweep))

    print(np.argmin([np.min(cover_distances[0]), np.min(cut_distances[0]), np.min(pull_distances[0]), np.min(sweep_distances[0])]))
    print(cover_distances, cut_distances, pull_distances, sweep_distances)


def assign_every_frame_octant():
    test_data = [np.load(f) for f in glob(str(Path(sys.argv[1])/'*.npy'))]
    test_data_occupancy = [utilities.find_occupancy_octant(i) for i in test_data]
    print(test_data_occupancy)

assign_every_frame_octant()

# print(template_poses_cover.shape)

# cover_nn = NearestNeighbors(n_neighbors=1).fit(template_poses_cover)
# cut_nn = NearestNeighbors(n_neighbors=1).fit(template_poses_cut)
# pull_nn = NearestNeighbors(n_neighbors=1).fit(template_poses_pull)
# sweep_nn = NearestNeighbors(n_neighbors=1).fit(template_poses_sweep)


# # min_cover_distance = np.ones(len(template_poses_cover[0]))

# test_data = sys.argv[1]

# for frame in glob(str(Path(test_data)/'*.npy')):
#     data = np.load(frame).flatten().reshape(1,-1)

#     cover_distance = cover_nn.kneighbors(data, return_distance=True)
#     cut_distance = cut_nn.kneighbors(data, return_distance=True)
#     pull_distance = pull_nn.kneighbors(data, return_distance=True)
#     sweep_distance = sweep_nn.kneighbors(data, return_distance=True)

#     print(cover_distance, cut_distance, pull_distance, sweep_distance)
