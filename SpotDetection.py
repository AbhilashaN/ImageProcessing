import cv2
import numpy as np


#cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

#font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)
img = cv2.imread('10.bmp')
while True:
    #ret, img=cam.read()
    
    img=cv2.resize(img,(340,220))

    #convert BGR to HSV
    imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,im = cv2.threshold(imgGray,230,255,cv2.THRESH_BINARY)
    #morphology
    #maskOpen=cv2.morphologyEx(im,cv2.MORPH_OPEN,kernelOpen)
    #maskClose=cv2.morphologyEx(im,cv2.MORPH_CLOSE,kernelClose)

    #maskFinal=maskClose
    conts,h=cv2.findContours(im,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    #cv2.drawContours(img,conts,-1,(255,0,0),3)
    (x,y),radius = cv2.minEnclosingCircle(conts)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(im,center,radius,(0,255,0),2)
    #x,y,w,h=cv2.boundingRect(conts)
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
        #cv2.cv.PutText(cv2.cv.fromarray(img), str(i+1),(x,y+h),font,(0,255,255))
    #cv2.imshow("maskClose",maskClose)
    #cv2.imshow("maskOpen",maskOpen)
    cv2.imshow("cam",img)
    k = cv2.waitKey(30)& 0xff
    if k == 27:
        break


cv2.destroyAllWindows()
