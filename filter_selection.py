import cv2
import numpy as np
import logger


def dilate(file, filter_value, img):
    try:

        # Reading the input image
        new_directory = "output"
        # Taking a matrix of size 5 as the kernel
        kernel = np.ones((filter_value, filter_value), np.uint8)

        logger.log("image : " + file + " dilatée")
        img_dilation = cv2.dilate(img, kernel,1)

        logger.log("image : " + file + " ajoutée au dossier : " + new_directory)
        return img_dilation

    except ValueError:
        if filter_value<0:
            print("erreur 2")


def blur(file, filter_value, img):
    try:
        new_directory = "output"
        blur_image = cv2.GaussianBlur(img, (filter_value, filter_value), 0)
        logger.log("image : " + file + " floutée")
        logger.log("image : " + file + " ajoutée au dossier : " + new_directory)
        return blur_image

    except cv2.error:

        print("Erreur de saisie du chemin")


def grayscayle(file, img):
    try:
        new_directory = "output"
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        logger.log("image : " + file + " convertie en noir et blanc")
        logger.log("image : " + file + " ajoutée au dossier : " + new_directory)
        return gray

    except cv2.error:

        print("Erreur de saisie du chemin")


def filter_application(filter_type, filter_value, file, img):
    if filter_type == "grayscale":
        test = grayscayle(file, img)
        return test
    elif filter_type == "blur":
        blur_img = blur(file, filter_value, img)
        return blur_img
    elif filter_type == "dilate":
        dilate_img = dilate(file, filter_value, img)
        return dilate_img
