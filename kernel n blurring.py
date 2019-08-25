import cv2
import numpy as np

def func(x):
    pass
       
org = cv2.imread('img1.jpg')

cv2.namedWindow('image',0)
cv2.createTrackbar('Blur','image',0,5,func)
while(1):
    blur = cv2.getTrackbarPos('Blur','image')

    if blur == 0:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(org,'BLUR LEVELS',(0,50), font, 1,(0,0,255),2)
        cv2.imshow('image',org)
    else:
        if blur == 1:
            blur = cv2.GaussianBlur(org,(3,3),0)
        elif blur == 2:
            blur = cv2.GaussianBlur(org,(5,5),0)
        elif blur == 3:
            blur = cv2.GaussianBlur(org,(7,7),0)
        elif blur == 4:
            blur = cv2.GaussianBlur(org,(9,9),0)
        else:
            blur = cv2.GaussianBlur(org,(11,11),0)

        cv2.imshow('image',blur)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break  
cv2.destroyAllWindows()
