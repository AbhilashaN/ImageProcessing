import cv2
import numpy as np

img = cv2.imread('img1.jpg')
retval,threshold = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
retval,threshold1 = cv2.threshold(img,250,255,cv2.THRESH_BINARY)

cv2.imshow('img',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold1',threshold1)

cv2.waitKey(0)
cv2.destroyAllWindows()
