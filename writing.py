import cv2
import logger

def write_file(new_directory, file, img):
    logger.log("image : " + file + " ajoutée au dossier : " + new_directory)
    cv2.imwrite(f"{new_directory}/{file}", img)