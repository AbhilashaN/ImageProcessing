import numpy as np
import cv2 
img = cv2.imread('img1.jpg')

blurImg51 = cv2.blur(img,(51,51))
blurImg3 = cv2.blur(img,(3,3))
blurImg5 = cv2.blur(img,(5,5))
blurImg7 = cv2.blur(img,(7,7))
blurImg9 = cv2.blur(img,(9,9))
blurImg11 = cv2.blur(img,(11,11))


cv2.imshow('blurImg3',blurImg3)
cv2.imshow('blurImg5',blurImg5)
cv2.imshow('blurImg7',blurImg7)
cv2.imshow('blurImg9',blurImg9)
cv2.imshow('blurImg11',blurImg11)
cv2.imshow('blurImg51',blurImg51)


cv2.waitKey(0)
cv2.destroyAllWindows()
