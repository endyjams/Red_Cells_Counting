import matplotlib.pyplot as plt
from read_images import ReadImages
from cells_detection import white_cells_detection as wcd
from cells_detection import red_cells_detection as rcd
import numpy as np
import cv2

def main():

    # Função para leitura das imagens
    images_list = ReadImages("archive/images")

    for pair in images_list:
        info = wcd.WhiteCellsDetection(pair[1])
        
        for info in info:
            print(str(pair[0]) + ',' + str(info[0]) + ',' + str(info[1]) + ',' + str(info[2]) + ',' + str(info[3]) + ',' + '"' + str(info[4]) + '"')

if __name__ == '__main__':
    main()