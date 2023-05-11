import numpy as np
import cv2

img = cv2.imread("/Users/kailashkumar/Downloads/Ex_Files_OpenCV_Python_Developers/Exercise Files/Ch04/04_06 Begin/faces.jpeg",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = "/Users/kailashkumar/Downloads/Ex_Files_OpenCV_Python_Developers/Exercise Files/Ch04/04_06 Begin/haarcascade_eye.xml"

eye_cascade = cv2.CascadeClassifier(path)

eyes = eye_cascade.detectMultiScale(gray, scaleFactor = 1.02, minNeighbors = 20, minSize = (10,10))
print(len(eyes))

for (x, y, w, h) in eyes:
    xc = (x + (x+w))/2
    yc = (y + (y+h))/2
    radius = w/2
    cv2.circle(img, (int(xc), int(yc)), int(radius), (255,0,0), 2)
    
cv2.imshow("Eyes", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
