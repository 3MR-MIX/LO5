import cv2
import numpy as np

img = np.ones((300, 300, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (50, 50), (250, 250), (0, 0, 0), 2)

seed_point = (100, 100)
fill_color = (0, 255, 0)

mask = np.zeros((302, 302), dtype=np.uint8)
cv2.floodFill(img, mask, seed_point, fill_color)

cv2.imshow('Flood Fill', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
