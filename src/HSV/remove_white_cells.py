import cv2
import numpy as np
import matplotlib.pyplot as plt

def RemoveWhiteCells(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Mantendo apenas as células brancas
    lower_red = np.array([140, 50, 50])
    upper_red = np.array([255, 255, 255])

    # Máscara que guarda o range que as células se encontram

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Agora, "limpa" os ruídos mínimos pretos e brancos que estão na imagem
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Segmentanto as células brancas, só elas irão aparecer
    result = cv2.bitwise_and(img, img, mask=mask)

    return result