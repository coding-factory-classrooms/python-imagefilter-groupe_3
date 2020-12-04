import cv2
import logger

def imread(src, file):
    img = cv2.imread(src)
    logger.log("image : " + file + " ouverte")
    return img