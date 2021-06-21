import cv2

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cam.read()
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    quit ='Press q to quit'
    cv2.imshow('frm',frame)
    cv2.putText(frame,quit,(350,30),font,1,(208,220,170))
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break

cam.release()
cv2.destroyAllWindows