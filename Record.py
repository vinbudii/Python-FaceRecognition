import cv2
import os

cam = cv2.VideoCapture(0)

cam.set(3, 640)
cam.set(4, 480)
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Face_data = 'Face_Data'

faceID = input("Input Face ID: ")
print("Taking 100 Data...")
data = 1

while True:
    ret, frame = cam.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(grey, 1.3, 5)

    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        namaFile = 'Face.'+str(faceID)+'.'+str(data)+'.jpg'
        cv2.imwrite(Face_data+'/'+namaFile,frame)
        data +=1

    cv2.imshow('record',frame)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break
    elif data > 100: 
        break

print('Sucess take data from face id',faceID)
cam.release()
cv2.destroyAllWindows