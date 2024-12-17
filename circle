import cv2
import numpy as np

image = np.ones((500, 500, 3), dtype=np.uint8) * 255

center_coordinates = (250, 250)
radius = 100

color = (255, 0, 0)
thickness = 5

cv2.circle(image, center_coordinates, radius, color, thickness)

cv2.imshow("circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
