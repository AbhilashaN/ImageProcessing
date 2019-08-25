import cv2
import numpy as np

img1 = cv2.imread('BG.jpg',1)
img2 = cv2.imread('BG1.png',1)
add = cv2.addWeighted(img1,0.8,img2,0.2,0)
cv2.imshow('added',add)
cv2.imwrite('adppbg.png',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
