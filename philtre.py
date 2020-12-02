import cv2
import numpy as np
import logger



def filtre_img(src, file):
    try:
        # Reading the input image
        new_directory = "output"

        img = cv2.imread(src)
        # Taking a matrix of size 5 as the kernel
        kernel = np.ones((5, 5), np.uint8)
        logger.log("image : " + file + " dilatée")
        img_dilation = cv2.dilate(img, kernel, iterations=1)

        cv2.imshow('Dilation', img_dilation)
        logger.log("image : " + file + " ajoutée au dossier : " + new_directory)
        cv2.imwrite(f"{new_directory}/{file}", img_dilation)
    except cv2.error :
        print("erreur")