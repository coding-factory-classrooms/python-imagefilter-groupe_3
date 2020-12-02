import cv2

def blur(src):
    img = cv2.imread(src)
    blur_image = cv2.GaussianBlur(img, (3,33),0)
    cv2.imshow('Blurred Image', blur_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

src = "imgs/schtroumpfette.jpg"
blur(src)