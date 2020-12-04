import cv2
import numpy as np
import logger


def dilate(src, file, filter_value):
    """
    Dilate une image
    :param src: source de l'image
    :param file: nom de l'image
    :param filter_value: l'intensité
    :return: ajoute l'image modifié dans un nouveau fichier
    """
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
    """
        Floute une image
        :param src: source de l'image
        :param file: nom de l'image
        :param filter_value: l'intensité du flou
        :return: ajoute l'image modifié dans un nouveau fichier
        """
    try:
        if filter_value % 2 != 0 and filter_value > 0:
            print(f"{filter_value} est impaire et positif ")
        else:
            print(f"{filter_value} est paire et/ou positif, erreur le nombre doit étre positif et impaire. ")
            return

        new_directory = "output"
        img = cv2.imread(src)
        blur_image = cv2.GaussianBlur(img, (filter_value, filter_value), 0)
        logger.log("image : " + file + " floutée")
        cv2.imshow('Blurred Image', blur_image)
        logger.log("image : " + file + " ajoutée au dossier : " + new_directory)
    except cv2.error:

        print("Erreur de saisie du chemin")

def grayscayle(src, file):
    """
        L'image est mise en noir et blanc
        :param src: source de l'image
        :param file: nom de l'image
        :return: ajoute l'image modifié dans un nouveau fichier
        """
    try:
        new_directory = "output"
        img = cv2.imread(src)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        logger.log("image : " + file + " convertie en noir et blanc")
        cv2.imshow('Gray image', gray)
        logger.log("image : " + file +" ajoutée au dossier : " + new_directory)
        cv2.imwrite(f"{new_directory}/{file}", gray)
    except cv2.error:

        print("Erreur de saisie du chemin")

def filter_application(filter_type, filter_value, src, file):
    """
    définition centrale qui appelle les différents filtres
    :param filter_type: le type du filtre (grayscale, blur ou dilate)
    :param filter_value: la valeur de l'intensité si le filtre en propose
    :param src: la source de l'image
    :param file: le nom de l'image
    """
    if filter_type == "grayscale":
        grayscayle(src, file)
    elif filter_type == "blur":
        blur(src, file, filter_value)
    elif filter_type == "dilate":
        dilate(src, file, filter_value)