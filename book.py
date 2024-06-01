import cv2
import numpy as np
from PIL import Image


input_image_path = 'apple.jpg'


colored_image = cv2.imread(input_image_path)
gray_image = cv2.cvtColor(colored_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edges = cv2.Canny(blurred_image, threshold1=30, threshold2=100)
outline_image = cv2.bitwise_not(edges)


cv2.imshow('Colored Image', colored_image)
cv2.imshow('Outline Image', outline_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
