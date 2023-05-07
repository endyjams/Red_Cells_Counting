import matplotlib.pyplot as plt
from read_images import ReadImages
import numpy as np
import cv2

def main():
    images_list = ReadImages()

    original_img = images_list[0]

    cht_img = original_img.copy()

    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    blurry_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    ret, binary_img = cv2.threshold(blurry_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    kernel = np.ones((3,3),np.uint8)
    closing_img = cv2.morphologyEx(binary_img,cv2.MORPH_CLOSE,kernel)
    opening_img = cv2.morphologyEx(closing_img,cv2.MORPH_OPEN,kernel)

    threshold_img = cv2.adaptiveThreshold(opening_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    cht = cv2.HoughCircles(
        threshold_img, 
        cv2.HOUGH_GRADIENT, 
        1,
        20,
        param1=50, 
        param2=30, 
        minRadius=0, 
        maxRadius=0
    )

    cht = np.uint16(np.around(cht))

    blood_cells = 0

    for i in cht[0,:]:
        x = i[0]
        y = i[1]
        r = i[2]

        if r <= 30:
            print("x pos: " + str(x))
            print("y pos: " + str(y))
            print("radius: " + str(r))
            cv2.circle(cht_img, (x, y), r, (0, 255, 0), 2)
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

    ax[1][1].imshow(closing_img)
    ax[1][1].set_title('Opening')

    ax[1][2].imshow(opening_img)
    ax[1][2].set_title('Closing')

    ax[2][0].imshow(threshold_img)
    ax[2][0].set_title('Threshold')

    ax[2][1].imshow(cht_img)
    ax[2][1].set_title('CHT => Circles: ' + str(blood_cells))

    plt.show()

if __name__ == '__main__':
    main()