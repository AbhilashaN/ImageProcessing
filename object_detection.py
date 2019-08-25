import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
i=0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,2,0.5,0,3,1)
while True :
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    print "Found {0} faces!".format(len(faces))
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray =gray[y:y+h,x:x+w]
        roi_color =frame[y:y+h,x:x+w]
        cv2.cv.PutText(cv2.cv.fromarray(frame),str(i+1),(x,y),font,(0,255,255))

        
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.cv.PutText(cv2.cv.fromarray(frame),str(i+1),(ex,ey),font,(255,0,255))

        print "Found {0} eyes!".format(len(eyes))   
    cv2.imshow('frame',frame)
    #print i
    k = cv2.waitKey(30)& 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

            
            
