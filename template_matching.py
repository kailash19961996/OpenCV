import numpy as np
import cv2

template = cv2.imread("/Users/kailashkumar/Downloads/Ex_Files_OpenCV_Python_Developers/Exercise Files/Ch04/04_03 Begin/template.jpg", 0)
image = cv2.imread("/Users/kailashkumar/Downloads/Ex_Files_OpenCV_Python_Developers/Exercise Files/Ch04/04_03 Begin/players.jpg", 0)

cv2.imshow("template", template)
cv2.imshow("image", image)

result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val, max_loc)
cv2.circle(result, max_loc, 15, 255, 2)
cv2.imshow("matching", result)

cv2.waitKey(1000)
cv2.destroyAllWindows()
