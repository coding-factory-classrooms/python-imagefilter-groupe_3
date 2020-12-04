import cv2
import logger

def write_file(new_directory, file, img):
    """
    Ajoute une image filtré dans un dossier
    :param new_directory: le dossier qui prend les images filtré
    :param file:
    :param img:
    """
    logger.log("image : " + file + " ajoutée au dossier : " + new_directory)
    cv2.imwrite(f"{new_directory}/{file}", img)