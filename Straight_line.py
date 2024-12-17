import cv2
import numpy as np

image = np.ones((500, 500, 3), dtype=np.uint8) * 255

start_point = (50, 100)
end_point = (400, 400)

color = (0, 0, 255)  
thickness = 5

cv2.line(image, start_point, end_point, color, thickness)


cv2.imshow('Straight Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
