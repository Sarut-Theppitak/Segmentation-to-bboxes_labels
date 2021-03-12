import cv2 
import os
import numpy as np
from natsort import natsorted

def xywh2xyxy(bbox):
    x, y, w, h = bbox
    x_min = int(x - (w/2))
    y_min = int(y - (h/2))
    x_max = int(x + (w/2))
    y_max = int(y + (h/2))

    return x_min, y_min, x_max, y_max

seg_mask_dir = f'./JPG'
label_dir = f'./labels'

segmask_list = os.listdir(seg_mask_dir)
segmask_list = natsorted(segmask_list)

for seg_maskfile_name in segmask_list:
    seg_maskfile = os.path.join(seg_mask_dir, seg_maskfile_name)
    label_file = os.path.join(label_dir, seg_maskfile_name.replace('.jpg', '.txt') )
    seg_mask = cv2.imread(seg_maskfile,0)
    seg_mask = np.copy(seg_mask)
    ori_h, ori_w = seg_mask.shape
    boxes = np.loadtxt(label_file).reshape(-1, 5)
    bboxes = boxes[:,1:]
    classes = boxes[:, 0]

    bboxes[:,::2] = bboxes[:,::2] * ori_w
    bboxes[:,1::2] = bboxes[:,1::2] * ori_h   
    bboxes = bboxes.astype('int')

    img = cv2.imread(seg_maskfile)
    im = np.copy(img)

    for bbox in bboxes:
        x_min, y_min, x_max, y_max = xywh2xyxy(bbox)
        cv2.rectangle(im, (x_min, y_min), (x_max, y_max) , (125,125,125), 2)

    filename = os.path.join(f'./gt_with_jpg', seg_maskfile_name)
    cv2.imwrite(filename, im)