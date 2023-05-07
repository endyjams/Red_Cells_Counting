import matplotlib.pyplot as plt
from read_images import ReadImages
from cells_detection import white_cells_detection as wcd
from cells_detection import red_cells_detection as rcd
import numpy as np
import cv2
from IOU import intersection_over_union as IOU

def main():

    iou_values = IOU.IntersectionOverUnion()


if __name__ == '__main__':
    main()