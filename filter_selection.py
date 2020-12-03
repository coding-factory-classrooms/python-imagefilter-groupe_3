import cv2
import numpy as np
import logger


def dilate(src, file, filter_value):
    try:
        # Reading the input image
        new_directory = "output"

        img = cv2.imread(src)
        # Taking a matrix of size 5 as the kernel
        kernel = np.ones((filter_value, filter_value), np.uint8)
        logger.log("image : " + file + " dilatée")
        img_dilation = cv2.dilate(img, kernel, iterations=1)

        cv2.imshow('Dilation', img_dilation)
        logger.log("image : " + file + " ajoutée au dossier : " + new_directory)


    except cv2.error :
        print("erreur")

def blur(src, file, filter_value):
    try:
        new_directory = "output"
        img = cv2.imread(src)
        blur_image = cv2.GaussianBlur(img, (filter_value,filter_value),0)
        logger.log("image : " + file + " floutée")
        cv2.imshow('Blurred Image', blur_image)
        logger.log("image : " + file + " ajoutée au dossier : " + new_directory)
    except cv2.error :

        print ("Erreur de saisie du chemin")

def grayscayle(src, file):
    try:
        new_directory = "output"
        img = cv2.imread(src)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        logger.log("image : " + file +" convertie en noir et blanc")
        cv2.imshow('Gray image', gray)
        logger.log("image : "+ file +" ajoutée au dossier : " + new_directory)
        cv2.imwrite(f"{new_directory}/{file}", gray)
    except cv2.error :

        print ("Erreur de saisie du chemin")

def filter_application(filter_type, filter_value, src, file):
    if filter_type == "grayscale":
        grayscayle(src, file)
    elif filter_type == "blur":
        blur(src, file, filter_value)
    elif filter_type=="dilate":
        dilate(src, file, filter_value)