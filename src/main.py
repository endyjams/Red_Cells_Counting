import matplotlib.pyplot as plt
from read_images import ReadImages
import numpy as np
import cv2

def main():
    # Read in list of images using ReadImages module
    images_list = ReadImages()

    # Select first image from list
    original_img = images_list[0]

    cht_img = original_img.copy()

    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    blurry_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    ret, binary_img = cv2.threshold(blurry_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    kernel = np.ones((3,3),np.uint8)
    opening_img = cv2.morphologyEx(binary_img,cv2.MORPH_OPEN,kernel, iterations = 2)
    dilate_img = cv2.dilate(opening_img,kernel,iterations=3)

    threshold_img = cv2.adaptiveThreshold(dilate_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    contours, hierarchy = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    blood_cells = 0

    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)

        if w > 10 and h > 10:
            cv2.rectangle(cht_img,(x,y),(x+w,y+h),(0,0,255),2)
            blood_cells += 1

    fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(10,7))
    fig.subplots_adjust(hspace= 0.5, wspace= 0.5)
    ax[0][0].imshow(original_img)
    ax[0][0].set_title('Original')

    ax[0][1].imshow(gray_img)
    ax[0][1].set_title('Gray')

    ax[0][2].imshow(blurry_img)
    ax[0][2].set_title('Gaussian Blur')

    ax[1][0].imshow(binary_img)
    ax[1][0].set_title('Binary')

    ax[1][1].imshow(opening_img)
    ax[1][1].set_title('Opening')

    ax[1][2].imshow(dilate_img)
    ax[1][2].set_title('Closing')

    ax[2][0].imshow(threshold_img)
    ax[2][0].set_title('Threshold')

    ax[2][1].imshow(cht_img)
    ax[2][1].set_title('CHT => Circles: ' + str(blood_cells))

    plt.show()

if __name__ == '__main__':
    main()