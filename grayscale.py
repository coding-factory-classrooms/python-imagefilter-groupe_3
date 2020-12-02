import cv2
import os
import logger

def grayscayle(src):
    try:
        new_directory = "output"
        img = cv2.imread(src)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        logger.log("image : " + src +" convertie en noir et blanc")
        cv2.imshow('Gray image', gray)
        logger.log("image : "+src+" ajoutée au dossier : " + new_directory)
        os.chdir(new_directory)
        cv2.imwrite("gray_img.jpg", gray)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except cv2.error :
        print ("Erreur de saisie du chemin")
