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

seg_mask_dir = f'./Ground_Truth'
out_dir = f'./labels'

segmask_list = os.listdir(seg_mask_dir)
segmask_list = natsorted(segmask_list)

for seg_maskfile_name in segmask_list:
    seg_maskfile = os.path.join(seg_mask_dir, seg_maskfile_name)
    seg_mask = cv2.imread(seg_maskfile,0)
    seg_mask = np.copy(seg_mask)
    ori_h, ori_w = seg_mask.shape
    ret,seg_mask = cv2.threshold(np.copy(seg_mask),127,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(seg_mask , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        cv2.drawContours(seg_mask,[c], 0, (255,255,255), -1)

    contours, hierarchy = cv2.findContours(seg_mask , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bboxes = []
    classes = []
    for c in contours:
        x_min, y_min, w, h = cv2.boundingRect(c)
        x_cen = x_min + (w/2)
        y_cen = y_min + (h/2)
        if (w / ori_w > 0.04) and (h / ori_h > 0.04):
            bboxes.append([x_cen, y_cen, w, h])
            classes.append(0)

    # save as .txt file yolo format 
    outfile = os.path.join(out_dir, seg_maskfile_name.replace('.tif', '.txt'))

    with open(outfile, 'w') as f:
        temp = []
        norm_bboxes = np.array(bboxes).astype('float32')
        norm_bboxes[:,::2] = norm_bboxes[:,::2] / ori_w
        norm_bboxes[:,1::2] = norm_bboxes[:,1::2] / ori_h

        temps = [' '.join([str(elem) for elem in bbox]) + '\n' for bbox in norm_bboxes]
        final_temps = [' '.join([str(clss), temp]) for temp, clss in zip(temps,classes)]
        f.writelines(final_temps)


    img = cv2.imread(seg_maskfile)
    im = np.copy(img)

    for bbox in bboxes:
        x_min, y_min, x_max, y_max = xywh2xyxy(bbox)
        cv2.rectangle(im, (x_min, y_min), (x_max, y_max) , (125,125,125), 2)


    filename = os.path.join(f'./results', seg_maskfile_name.replace('.tif', '.jpg'))
    cv2.imwrite(filename, im)

    # cv2.imshow(seg_maskfile_name, im) 
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
