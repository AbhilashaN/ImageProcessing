import cv2
import numpy as np

img = cv2.imread('corner.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,50,0.01,20)
corners = np.int0(corners)
print "Found {0} corners!".format(len(corners))//for printing number of corners.
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),5,255,-1)
    

cv2.imshow('corner',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
