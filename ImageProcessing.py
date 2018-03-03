import cv2
import numpy as np

image= cv2.imread('img.jpg')
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(image, kernel, iterations=1)
dilation = cv2.dilate(image, kernel, iterations=1)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Input',image)
cv2.imshow('Erosion',erosion)
cv2.imshow('Dilation',dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.imshow('Gradient',gradient)

cv2.waitKey(0)
