import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

gray = cv.imread("machupicchu.jpg",0)
color = cv.imread("machupicchu.jpg",0)

gray = cv.blur(gray, (5,5))

edges = cv.Canny(gray,100,220)

plt.figure(figsize=(12,6))
plt.imshow(edges, cmap='gray')

# plt.show()

lines = cv.HoughLinesP(edges, 2, np.pi/180, 490, minLineLength=100, maxLineGap=15)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(color, (x1, y1), (x2, y2), (0, 255, 0), 2)  

plt.figure(figsize=(12,6))
plt.imshow(color[...,::-1])
plt.show()
print(lines)