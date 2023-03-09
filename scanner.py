import cv2
import pyzbar.pyzbar as pyzbar

#decode image

img = cv2.imread('img.png')

decodedObjects = pyzbar.decode(img)
print(decodeObjects)
