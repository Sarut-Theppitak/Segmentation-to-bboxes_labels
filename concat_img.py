import os
import numpy as np
import cv2

gt_dir = f'./gt_with_jpg'
result_dir = f'./test_results'
compare_dir = f'./comparisons'

gt_list = os.listdir(gt_dir)

for img_name in gt_list:

    gt_img_path = os.path.join(gt_dir,img_name)
    result_img_path = os.path.join(result_dir,img_name)
    compare_path = os.path.join(compare_dir,img_name)


    gt_img = cv2.imread(gt_img_path)
    result_img = cv2.imread(result_img_path)

    vis = np.concatenate((gt_img, result_img), axis=1)

    cv2.imwrite(compare_path, vis)
    print(compare_path)
    # cv2.imshow(img_name, vis) 
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

