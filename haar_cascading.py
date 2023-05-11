import numpy as np
import cv2

img = cv2.imread("/Users/kailashkumar/Downloads/Ex_Files_OpenCV_Python_Developers/Exercise Files/Ch04/04_06 Begin/faces.jpeg",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "/Users/kailashkumar/Downloads/Ex_Files_OpenCV_Python_Developers/Exercise Files/Ch04/04_06 Begin/haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(path)

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5, minSize = (10,10))
print(len(faces))

for (x, y, w, h) in faces:
    cv2.circle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Image", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()