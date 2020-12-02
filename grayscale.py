import cv2
import logger

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
