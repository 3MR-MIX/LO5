import cv2
import numpy as np

img = np.ones((300,300,3),dtype=np.uint8)
cv2.rectangle(img,(100,100),(200,200),(0,255,0),-1)

center = (img.shape[1] // 2,img.shape[0]//1)
angle = 45
scale = 1.0

rotation_matrix = cv2.getRotationMatrix2D(center,angle,scale)
rotation_img = cv2.warpAffine(img,rotation_matrix,(img.shape[1],img.shape[0]))

cv2.imshow('Original Image',img)
cv2.imshow('Scaled Image',rotation_img)
cv2.waitKey(0)
cv2.destroyWindow()

