import cv2
import numpy as np
import serial
import time

connected = False
ser=serial.Serial("COM3",9600,timeout=5)
while not connected:
    serin = ser.read()
    connected = True
i=10
kernelClose=np.ones((20,20))
while(1):
    im = cv2.imread("10.bmp")
    cv2.imshow('im',im)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY);
    ret,image = cv2.threshold(imgray,210,255,cv2.THRESH_BINARY);
    cv2.imshow('image',image)
    one = image[0:320,0:80]
    two = image[0:320,81:160]
    three = image[0:320,161:239]
    no1 = cv2.countNonZero(one)
    maxi = no1
    no2 = cv2.countNonZero(two)
    if no2 > maxi:
        maxi = no2
    no3 = cv2.countNonZero(three)
    if no3 > maxi:
        maxi = no3
    print no1,no2,no3,maxi    
    cv2.imshow('one',one)
    cv2.imshow('two',two)
    cv2.imshow('three',three)
    #maskClose=cv2.morphologyEx(two,cv2.MORPH_CLOSE,kernelClose)
    #cimage,contours,hierarchy=cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #ellipse=cv2.fitEllipse(contours)
    #ellipse_final=c2.ellipse(cimage,ellipse,(0,255,0),2)
    #cv2.imshow('cimage',cimage)
    if maxi==no1:
        ser.write('1')
    elif maxi==no2:
        print "2"
        ser.write('2')
        
    elif maxi==no3:
        ser.write('3')
    k=cv2.waitKey(0)  
    if(k==27):
        break
while ser.read() == '1':
     ser.read()
ser.close()    
cv2.destroyAllWindows()
