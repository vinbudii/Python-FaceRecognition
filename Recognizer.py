import cv2
import os
import numpy as np
from datetime import datetime

Face_data = 'Face_Data'
Train_data = 'Face_Train'

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
minWidth = 0.1*cam.get(3)
minHeight = 0.1*cam.get(4)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
faceRecognizer.read(Train_data+'/trainer.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
id = 0
names = ['Unknown','ID#1','ID#2','ID#3']

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

while True:
    ret, frame = cam.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(grey, 1.1, 5,minSize=(round(minWidth),round(minHeight)))
    quit ='Press q to quit'

    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        id, confidence = faceRecognizer.predict(grey[y:y+h,x:x+w])
        if confidence <= 50 :
            nameID = names[id]
            confidenceTxt = "{0}%".format(round(100-confidence))
            markAttendance(names[id])
        else:
            nameID = names[0]
            confidenceTxt = "{0}%".format(round(100-confidence))
        cv2.putText(frame,str(nameID),(x+5,y-5),font,1,(255,255,255),2)
        cv2.putText(frame,str(confidenceTxt),(x+5,y+h-5),font,1,(255,255,255),1)                         

    cv2.putText(frame,quit,(350,30),font,1,(208,220,170))
    cv2.imshow('Recog',frame)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break

print("EXIT")
cam.realease()
cv2.destroyAllWindows