import cv2
import numpy as np

org = cv2.imread('img1.jpg')

print "Enter level of blurriness from 0-5"
size = input()
if size == 0:
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(org,'This shows the original image',(0,100), font, 1,(0,0,255),2)
    cv2.imshow('original',org)
else:    
    if size == 1:
        blur = cv2.GaussianBlur(org,(5,5),0)
    elif size == 2:
        blur = cv2.GaussianBlur(org,(9,9),0)
    elif size == 3:
        blur = cv2.GaussianBlur(org,(11,11),0)
    elif size == 4:
        blur = cv2.GaussianBlur(org,(15,15),0)
    else:
        blur = cv2.GaussianBlur(org,(21,21),0)

    cv2.imshow('blur',blur)
    cv2.imshow('orginal',org)

cv2.waitKey(0)
cv2.destroyAllWindows()
