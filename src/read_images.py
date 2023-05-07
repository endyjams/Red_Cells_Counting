import cv2
import glob
import os
import matplotlib.pyplot as plt
import numpy as np

def ReadImages(directory):
    image_files = sorted(glob.glob(os.path.join(directory, '*.png')))
    
    images = []

    for img_file in image_files:
        img = cv2.imread(img_file, cv2.IMREAD_COLOR)
        name = '"' + str(img_file.removeprefix(directory + '/')) + '"'
        images.append((name, img))
    
    return images