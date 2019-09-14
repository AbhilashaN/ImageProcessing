import cv2
import numpy as np
#read images
img1 = cv2.imread('img3.jpg',1)
img2 = cv2.imread('img1.jpg',1)
img3 = cv2.imread('img4.jpg',1)

#add = img1 + img2
#add = cv2.add(img1,img2)
#weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)
#cv2.imshow('weighted',weighted)
rows,cols,channels = img3.shape
roi = img1[0:rows,0:cols]
img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
img2grayy = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#create mask
ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
ret,maskk = cv2.threshold(img2grayy,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow('img2grayy',img2grayy)
cv2.imshow('img2gray',img2gray)
cv2.imshow('mask',mask)
cv2.imshow('maskk',maskk)
cv2.waitKey(0)
cv2.destroyAllWindows()
