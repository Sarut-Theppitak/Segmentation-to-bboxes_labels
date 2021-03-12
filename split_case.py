import os
import argparse
import shutil
from sklearn.model_selection import train_test_split
from natsort import natsorted
import random
import math
import numpy as np

cases = [
    list(range(1,26)), 
    list(range(26,51)), 
    list(range(51,79)),
    list(range(79,98)),
    list(range(98,104)),
    list(range(104,127)),
    list(range(127,152)),
    list(range(152,173)),
    list(range(173,178)),
    list(range(178,200)),
    list(range(200,206)),
    list(range(206,228)),
    list(range(228,253)),
    list(range(253,278)),
    list(range(278,298)),
    list(range(298,318)),
    list(range(318,343)),
    list(range(343,364)),
    list(range(364,384)),
    list(range(384,409)),
    list(range(409,429)),
    list(range(429,467)),
    list(range(467,479)),
    list(range(479,504)),
    ]

ratios = [0.1, 0.15, 0.2, 0.25, 0.3]
train_data = {}
valid_data = {}

seedd = 1
for ratio in ratios:
    random.seed(seedd)
    valid_list = [random.sample(case, round(len(case) * ratio)) for case in cases]
    valid_list = [num for ele in valid_list for num in ele]
    valid_list = natsorted(valid_list)
    valid_data[ratio] = valid_list

    all_list = list(range(1,504))
    train_list = np.setdiff1d(all_list, valid_list)
    train_data[ratio] = train_list

    train_temp = [str(num) + '\n' for num in train_list]
    valid_temp = [str(num) + '\n' for num in valid_list]

    with open(os.path.join('./split_case',f'train_seed{seedd}_{int(ratio*100)}.txt'), 'w') as f:
        f.writelines(train_temp)
    with open(os.path.join('./split_case',f'valid_seed{seedd}_{int(ratio*100)}.txt'), 'w') as f:
        f.writelines(valid_temp)





