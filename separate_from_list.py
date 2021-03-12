import os
import argparse
import shutil
from sklearn.model_selection import train_test_split
from natsort import natsorted
import random
import math
import numpy as np

image_dir = f'./JPG'
label_dir = f'./labels'
train_dir = f'./train'
valid_dir = f'./valid'


image_names = os.listdir(image_dir)

with open(f'./split_case/train_seed1_20.txt', 'r') as f:
    lines = f.readlines()
train_ind = [int(x.strip()) for x in lines]

with open(f'./split_case/valid_seed1_20.txt', 'r') as f:
    lines = f.readlines()
valid_ind = [int(x.strip()) for x in lines]

# Create all folders
if os.path.exists(train_dir):
    shutil.rmtree(train_dir)  # delete directory

if os.path.exists(valid_dir):
    shutil.rmtree(valid_dir)  # delete directory

image_train_dir = os.path.join(train_dir,'images')
os.makedirs(image_train_dir)

label_train_dir = os.path.join(train_dir,'labels')
os.makedirs(label_train_dir)

image_valid_dir = os.path.join(valid_dir,'images')
os.makedirs(image_valid_dir)

label_valid_dir = os.path.join(valid_dir,'labels')
os.makedirs(label_valid_dir)


image_names = natsorted(image_names)
for image_name in image_names:
    ind = int(image_name.split('.jpg')[0])
    image_path = os.path.join(image_dir, image_name)
    label_path = os.path.join(label_dir, image_name.replace('.jpg','.txt'))
    if ind in train_ind:
        copy_image_path = os.path.join(image_train_dir, image_name)
        copy_label_path = os.path.join(label_train_dir, image_name.replace('.jpg','.txt'))
    elif ind in valid_ind:
        copy_image_path = os.path.join(image_valid_dir, image_name)
        copy_label_path = os.path.join(label_valid_dir, image_name.replace('.jpg','.txt'))        

    if ind <= 503:

        shutil.copy(image_path, copy_image_path)
        shutil.copy(label_path, copy_label_path)

