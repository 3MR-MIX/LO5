import cv2
import numpy as np

img = np.ones((400, 400, 3), dtype=np.uint8) * 255

x_min, y_min = 100, 100
x_max, y_max = 300, 300

cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

x1, y1 = 50, 50
x2, y2 = 350, 350
x1 = max(x1, x_min)
x2 = min(x2, x_max)
y1 = max(y1, y_min)
y2 = min(y2, y_max)
cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

x1, y1 = 150, 50
x2, y2 = 150, 350
x1 = max(x1, x_min)
x2 = min(x2, x_max)
y1 = max(y1, y_min)
y2 = min(y2, y_max)
cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("Clipping Simulation", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
