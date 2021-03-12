import cv2 
import os
import tifffile as tiff

image_dir = f'./Original'
new_image_dir = f'./JPG'

if os.path.exists(new_image_dir):
    shutil.rmtree(new_image_dir)
os.makedirs(new_image_dir)   

image_names = os.listdir(image_dir)
for image_name in image_names:
    ind = int(image_name.split('.tif')[0])
    image_path = os.path.join(image_dir, image_name)

    im = tiff.imread(image_path)
    tiff.imsave(os.path.join(new_image_dir, f'{ind}.jpg'), im)