import cv2
import numpy as np

img = np.ones((400, 400, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 2)

cv2.line(img, (50, 50), (350, 350), (0, 255, 0), 2)
cv2.line(img, (150, 50), (150, 350), (0, 0, 255), 2)

cv2.imshow("Clipping Simulation", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
