import cv2
import logger

def blur(src, file):
    try:
        new_directory = "output"
        img = cv2.imread(src)
        blur_image = cv2.GaussianBlur(img, (3,33),0)
        logger.log("image : " + file + " floutée")
        cv2.imshow('Blurred Image', blur_image)
        logger.log("image : " + file + " ajoutée au dossier : " + new_directory)
        cv2.imwrite(f"{new_directory}/{file}", blur_image)
    except cv2.error :

        print ("Erreur de saisie du chemin")



